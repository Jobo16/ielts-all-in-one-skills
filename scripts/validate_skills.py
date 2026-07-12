#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: unclosed YAML frontmatter")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, separator, value = line.partition(":")
        if not separator or not key.strip() or not value.strip():
            raise ValueError(f"{path}: invalid frontmatter line: {line}")
        fields[key.strip()] = value.strip().strip('"')
    return fields


def validate_skill(skill_dir: Path) -> dict[str, object]:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise ValueError(f"{skill_dir}: missing SKILL.md")
    fields = parse_frontmatter(skill_file)
    if set(fields) != {"name", "description"}:
        raise ValueError(f"{skill_file}: frontmatter must contain only name and description")
    if fields["name"] != skill_dir.name:
        raise ValueError(f"{skill_file}: name must match directory")
    if not NAME_PATTERN.fullmatch(fields["name"]):
        raise ValueError(f"{skill_file}: invalid skill name")
    if len(fields["description"]) < 40:
        raise ValueError(f"{skill_file}: description is too short")

    openai_file = skill_dir / "agents" / "openai.yaml"
    if not openai_file.is_file():
        raise ValueError(f"{skill_dir}: missing agents/openai.yaml")
    openai_text = openai_file.read_text(encoding="utf-8")
    if f"${fields['name']}" not in openai_text:
        raise ValueError(f"{openai_file}: default_prompt must mention ${fields['name']}")
    skill_manifest = json.loads((skill_dir / "manifest.json").read_text(encoding="utf-8"))
    if skill_manifest.get("id") != fields["name"]:
        raise ValueError(f"{skill_dir}: manifest id must match Skill name")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(skill_manifest.get("version", ""))):
        raise ValueError(f"{skill_dir}: manifest version must be stable semver")
    for script in ("learning_store.py", "update_skill.py"):
        if not (skill_dir / "scripts" / script).is_file():
            raise ValueError(f"{skill_dir}: missing scripts/{script}")
    return skill_manifest


def main() -> None:
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        raise ValueError("no skills found")
    skill_manifests = {skill_dir.name: validate_skill(skill_dir) for skill_dir in skill_dirs}

    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    manifest_skills = {item["id"] for item in manifest["skills"]}
    directory_skills = {path.name for path in skill_dirs}
    if manifest_skills != directory_skills:
        raise ValueError("manifest skills do not match skills directory")
    for skill_id, skill_manifest in skill_manifests.items():
        if skill_manifest["version"] != manifest["version"]:
            raise ValueError(f"{skill_id}: Skill and repository versions differ")

    forbidden = list(ROOT.rglob("*.pdf")) + list(ROOT.rglob(".env"))
    if forbidden:
        raise ValueError(f"forbidden files: {forbidden}")
    print(f"validated {len(skill_dirs)} skill(s)")


if __name__ == "__main__":
    main()
