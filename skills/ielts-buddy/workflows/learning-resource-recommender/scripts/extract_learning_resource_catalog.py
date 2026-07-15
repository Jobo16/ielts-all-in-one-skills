#!/usr/bin/env python3
"""Extract resource candidates from a Markdown learning-resource catalog."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_CATALOG = Path(__file__).resolve().parents[1] / "references" / "learning-english-catalog.md"

LINK_RE = re.compile(r"-\s*\[([^\]]+)\]\((https?://[^)]+)\)\s*(?:-\s*(.*))?$")
HEADING_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$")

SKILL_KEYWORDS = {
    "listening": ["听力", "播客", "电台", "asmr", "podcast", "radio", "listening", "sounds"],
    "speaking": ["口语", "发音", "conversation", "speaking", "pronunciation", "voice"],
    "reading": ["阅读", "新闻", "小说", "漫画", "reading", "news", "book"],
    "writing": ["写作", "作文", "writing", "essay"],
    "vocabulary": ["词汇", "单词", "vocabulary", "words", "phrases"],
    "grammar": ["语法", "grammar"],
    "ielts": ["雅思", "ielts", "应试", "exam"],
    "video": ["视频", "youtube", "bilibili", "ted", "video"],
    "course": ["课程", "在线课程", "course"],
}


def clean(text: str) -> str:
    text = re.sub(r"[#🎙️💻🎤🙊📻🎧🎥📺📼📰📚👾🎮🛜ʙ📖]", "", text)
    return " ".join(text.strip().split())


def infer_skills(text: str) -> list[str]:
    source = text.lower()
    skills = []
    for skill, keywords in SKILL_KEYWORDS.items():
        if any(keyword.lower() in source for keyword in keywords):
            skills.append(skill)
    return skills


def parse_catalog(path: Path) -> list[dict[str, Any]]:
    headings: dict[int, str] = {}
    items: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        heading = HEADING_RE.match(line)
        if heading:
            level = len(heading.group(1))
            headings[level] = clean(heading.group(2))
            for stale in [key for key in headings if key > level]:
                del headings[stale]
            continue
        match = LINK_RE.match(line.strip())
        if not match:
            continue
        title, url, description = match.groups()
        section_path = [headings[key] for key in sorted(headings)]
        text_for_tags = " ".join([title, description or "", " / ".join(section_path)])
        items.append(
            {
                "title": clean(title),
                "url": url.strip(),
                "description": clean(description or ""),
                "section_path": section_path,
                "category": " / ".join(section_path),
                "skills": infer_skills(text_for_tags),
                "line": line_number,
            }
        )
    return items


def score(item: dict[str, Any], skill: str | None, query: str | None) -> int:
    value = 0
    if skill and skill in item.get("skills", []):
        value += 10
    blob = " ".join(
        [
            str(item.get("title", "")),
            str(item.get("description", "")),
            str(item.get("category", "")),
            " ".join(item.get("skills", [])),
        ]
    ).lower()
    if query:
        for token in re.findall(r"[\w\u4e00-\u9fff]+", query.lower()):
            if token and token in blob:
                value += 2
    if "ielts" in item.get("skills", []):
        value += 2
    if "bbc" in blob or "voa" in blob or "british council" in blob:
        value += 1
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", choices=sorted(SKILL_KEYWORDS), default=None)
    parser.add_argument("--query", default=None)
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    items = parse_catalog(DEFAULT_CATALOG)
    if args.skill or args.query:
        items = sorted(items, key=lambda item: score(item, args.skill, args.query), reverse=True)
        items = [item for item in items if score(item, args.skill, args.query) > 0]
    items = items[: max(1, args.limit)]
    payload = {
        "source": str(DEFAULT_CATALOG),
        "count": len(items),
        "items": items,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
