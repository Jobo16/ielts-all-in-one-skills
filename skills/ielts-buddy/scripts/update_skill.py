#!/usr/bin/env python3
"""Install, inspect, check, and atomically update the IELTS Buddy Skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
import uuid
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

SKILL_ID = "ielts-buddy"
STATE_SCHEMA_VERSION = 1
CHECK_INTERVAL = timedelta(hours=24)
DEFAULT_MANIFEST_URL = "https://ieltsbuddy.igocn.cn/api/public/skills/manifest"
VERSION_PATTERN = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")


def skill_directory() -> Path:
    return Path(__file__).resolve().parents[1]


def state_path() -> Path:
    home = Path(os.environ.get("IELTS_BUDDY_HOME", Path.home() / ".ielts-buddy"))
    return home / "skill-install.json"


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_datetime(value: datetime | None = None) -> str:
    return (value or utc_now()).astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def version_tuple(value: str) -> tuple[int, int, int]:
    match = VERSION_PATTERN.fullmatch(value.strip())
    if not match:
        raise ValueError(f"Invalid stable version: {value}")
    return tuple(int(part) for part in match.groups())


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return value


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def validate_skill(source: Path, expected_version: str | None = None) -> dict[str, Any]:
    manifest_path = source / "manifest.json"
    skill_path = source / "SKILL.md"
    updater_path = source / "scripts" / "update_skill.py"
    learning_store_path = source / "scripts" / "learning_store.py"
    for required in (manifest_path, skill_path, updater_path, learning_store_path):
        if not required.is_file():
            raise ValueError(f"Skill package is missing {required.relative_to(source)}")
    manifest = read_json(manifest_path)
    if manifest.get("id") != SKILL_ID:
        raise ValueError("Skill package id is invalid")
    version = str(manifest.get("version", ""))
    version_tuple(version)
    if expected_version and version_tuple(version) != version_tuple(expected_version):
        raise ValueError(f"Skill package version {version} does not match {expected_version}")
    frontmatter = skill_path.read_text(encoding="utf-8").split("---", 2)
    if len(frontmatter) < 3 or "name: ielts-buddy" not in frontmatter[1]:
        raise ValueError("SKILL.md frontmatter is invalid")
    return manifest


def installed_status(target: Path, install_state: Path) -> dict[str, Any]:
    manifest = validate_skill(target)
    state = read_json(install_state) if install_state.is_file() else {}
    return {
        "skillId": SKILL_ID,
        "version": manifest["version"],
        "eventSchemaVersion": manifest.get("eventSchemaVersion", 1),
        "channel": manifest.get("channel", "stable"),
        "installPath": str(target),
        "statePath": str(install_state),
        "lastCheckedAt": state.get("lastCheckedAt"),
        "lastUpdatedAt": state.get("lastUpdatedAt"),
    }


def evaluate_update(target: Path, service_manifest: dict[str, Any]) -> dict[str, Any]:
    local = validate_skill(target)
    contract = service_manifest.get("update")
    if not isinstance(contract, dict):
        raise ValueError("Service manifest does not contain an update contract")
    latest = str(contract.get("latestVersion", ""))
    minimum = str(contract.get("minimumSupportedVersion", ""))
    local_version = str(local["version"])
    local_tuple = version_tuple(local_version)
    latest_tuple = version_tuple(latest)
    minimum_tuple = version_tuple(minimum)
    package = contract.get("package")
    package_ready = isinstance(package, dict) and bool(package.get("url")) and bool(package.get("sha256"))
    return {
        "skillId": SKILL_ID,
        "channel": contract.get("channel", "stable"),
        "localVersion": local_version,
        "latestVersion": latest,
        "minimumSupportedVersion": minimum,
        "eventSchemaVersion": contract.get("eventSchemaVersion", 1),
        "supported": local_tuple >= minimum_tuple,
        "updateAvailable": latest_tuple > local_tuple,
        "packageReady": package_ready,
        "package": package if package_ready else None,
    }


def fetch_service_manifest(url: str) -> dict[str, Any]:
    if urlparse(url).scheme != "https":
        raise ValueError("Service manifest URL must use HTTPS")
    request = urllib.request.Request(url, headers={"User-Agent": "ielts-buddy-skill-updater"})
    with urllib.request.urlopen(request, timeout=20) as response:
        value = json.load(response)
    if not isinstance(value, dict):
        raise ValueError("Service manifest response is invalid")
    return value


def check_for_update(
    target: Path,
    install_state: Path,
    manifest_url: str,
    force: bool = False,
) -> dict[str, Any]:
    current = validate_skill(target)
    state = read_json(install_state) if install_state.is_file() else {}
    last_checked = state.get("lastCheckedAt")
    cached = state.get("lastCheck")
    if not force and last_checked and isinstance(cached, dict):
        checked_at = datetime.fromisoformat(str(last_checked).replace("Z", "+00:00"))
        if utc_now() - checked_at < CHECK_INTERVAL and cached.get("localVersion") == current["version"]:
            return {**cached, "cached": True}
    result = evaluate_update(target, fetch_service_manifest(manifest_url))
    state.update({
        "schemaVersion": STATE_SCHEMA_VERSION,
        "skillId": SKILL_ID,
        "version": current["version"],
        "installPath": str(target),
        "channel": "stable",
        "lastCheckedAt": iso_datetime(),
        "lastCheck": result,
    })
    write_json_atomic(install_state, state)
    return {**result, "cached": False}


def install_from_directory(source: Path, target: Path, install_state: Path) -> dict[str, Any]:
    target = target.expanduser().resolve()
    install_state = install_state.expanduser().resolve()
    manifest = validate_skill(source)
    replace_skill_directory(source, target)
    now = iso_datetime()
    state = {
        "schemaVersion": STATE_SCHEMA_VERSION,
        "skillId": SKILL_ID,
        "version": manifest["version"],
        "installPath": str(target),
        "channel": manifest.get("channel", "stable"),
        "installedAt": now,
        "lastUpdatedAt": now,
    }
    write_json_atomic(install_state, state)
    return installed_status(target, install_state)


def apply_update(
    target: Path,
    install_state: Path,
    service_manifest: dict[str, Any],
    allow_file_url: bool = False,
) -> dict[str, Any]:
    target = target.expanduser().resolve()
    install_state = install_state.expanduser().resolve()
    update = evaluate_update(target, service_manifest)
    if not update["updateAvailable"]:
        return {**update, "updated": False}
    if not update["packageReady"]:
        raise ValueError("Update package is not ready")
    package = update["package"]
    assert isinstance(package, dict)
    with tempfile.TemporaryDirectory(prefix="ielts-buddy-update-") as temporary:
        temp_dir = Path(temporary)
        archive = temp_dir / "release-package"
        download_file(str(package["url"]), archive, allow_file_url)
        verify_sha256(archive, str(package["sha256"]))
        extracted = temp_dir / "extracted"
        extracted.mkdir()
        extract_archive(archive, extracted)
        source = find_skill_directory(extracted)
        manifest = validate_skill(source, str(update["latestVersion"]))
        replace_skill_directory(source, target)
    previous = read_json(install_state) if install_state.is_file() else {}
    now = iso_datetime()
    state = {
        **previous,
        "schemaVersion": STATE_SCHEMA_VERSION,
        "skillId": SKILL_ID,
        "version": manifest["version"],
        "installPath": str(target),
        "channel": manifest.get("channel", "stable"),
        "installedAt": previous.get("installedAt", now),
        "lastUpdatedAt": now,
        "lastCheckedAt": now,
        "lastCheck": {**update, "localVersion": manifest["version"], "updateAvailable": False},
    }
    write_json_atomic(install_state, state)
    return {**update, "updated": True, "version": manifest["version"]}


def apply_latest(target: Path, install_state: Path, manifest_url: str) -> dict[str, Any]:
    return apply_update(target, install_state, fetch_service_manifest(manifest_url))


def replace_skill_directory(source: Path, target: Path) -> None:
    source = source.resolve()
    target = target.expanduser().resolve()
    if source == target:
        raise ValueError("Source and target Skill directories must differ")
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = target.parent / f".{target.name}.stage-{uuid.uuid4().hex}"
    backup = target.parent / f".{target.name}.backup-{uuid.uuid4().hex}"
    shutil.copytree(source, stage, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    validate_skill(stage)
    had_target = target.exists()
    try:
        if had_target:
            os.replace(target, backup)
        os.replace(stage, target)
        run_post_install(target)
    except Exception:
        if stage.exists():
            shutil.rmtree(stage)
        if target.exists():
            shutil.rmtree(target)
        if had_target and backup.exists():
            os.replace(backup, target)
        raise
    if backup.exists():
        shutil.rmtree(backup)


def run_post_install(target: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(target / "scripts" / "learning_store.py"), "init"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Learning store migration failed")


def download_file(url: str, destination: Path, allow_file_url: bool = False) -> None:
    scheme = urlparse(url).scheme
    if scheme != "https" and not (allow_file_url and scheme == "file"):
        raise ValueError("Update package URL must use HTTPS")
    request = urllib.request.Request(url, headers={"User-Agent": "ielts-buddy-skill-updater"})
    with urllib.request.urlopen(request, timeout=30) as response, destination.open("wb") as output:
        shutil.copyfileobj(response, output)


def verify_sha256(path: Path, expected: str) -> None:
    normalized = expected.strip().lower()
    if not re.fullmatch(r"[0-9a-f]{64}", normalized):
        raise ValueError("Update package SHA-256 is invalid")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != normalized:
        raise ValueError("Update package SHA-256 does not match")


def extract_archive(archive: Path, destination: Path) -> None:
    if tarfile.is_tarfile(archive):
        with tarfile.open(archive) as package:
            members = package.getmembers()
            if any(not (member.isfile() or member.isdir()) for member in members):
                raise ValueError("Update package may contain only files and directories")
            for member in members:
                ensure_within(destination, destination / member.name)
            package.extractall(destination, members=members)
        return
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as package:
            for member in package.infolist():
                ensure_within(destination, destination / member.filename)
            package.extractall(destination)
        return
    raise ValueError("Update package must be a tar or zip archive")


def ensure_within(root: Path, path: Path) -> None:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as error:
        raise ValueError("Update package contains an unsafe path") from error


def find_skill_directory(root: Path) -> Path:
    candidates = [path.parent for path in root.rglob("manifest.json") if (path.parent / "SKILL.md").is_file()]
    valid = [path for path in candidates if read_json(path / "manifest.json").get("id") == SKILL_ID]
    if len(valid) != 1:
        raise ValueError("Update package must contain exactly one IELTS Buddy Skill")
    return valid[0]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("status", "check", "apply"):
        child = commands.add_parser(command)
        child.add_argument("--target", type=Path, default=skill_directory())
        child.add_argument("--state", type=Path, default=state_path())
        if command in ("check", "apply"):
            child.add_argument("--manifest-url", default=DEFAULT_MANIFEST_URL)
        if command == "check":
            child.add_argument("--force", action="store_true")
    install = commands.add_parser("install")
    install.add_argument("--source", type=Path, default=skill_directory())
    install.add_argument("--target", type=Path, required=True)
    install.add_argument("--state", type=Path, default=state_path())
    return parser


def run(args: argparse.Namespace) -> dict[str, Any]:
    if args.command == "status":
        return installed_status(args.target, args.state)
    if args.command == "check":
        return check_for_update(args.target, args.state, args.manifest_url, args.force)
    if args.command == "apply":
        return apply_latest(args.target, args.state, args.manifest_url)
    if args.command == "install":
        return install_from_directory(args.source, args.target, args.state)
    raise ValueError(f"Unknown command: {args.command}")


def main() -> None:
    try:
        print(json.dumps(run(build_parser().parse_args()), ensure_ascii=False, indent=2))
    except (ValueError, OSError, sqlite3.Error, RuntimeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
