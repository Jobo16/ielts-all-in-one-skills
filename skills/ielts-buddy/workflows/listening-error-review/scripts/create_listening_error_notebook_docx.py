#!/usr/bin/env python3
"""Create an IELTS Listening error notebook DOCX from a JSON plan."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
from simple_docx import SimpleDocx, normalize_spaces, word_count  # noqa: E402


def dicts(value: Any) -> list[dict[str, Any]]:
    return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []


def strings(value: Any) -> list[str]:
    return [normalize_spaces(item) for item in value if normalize_spaces(item)] if isinstance(value, list) else []


def default_output(plan_path: Path) -> Path:
    desktop = Path.home() / "Desktop"
    stamp = datetime.now().strftime("%Y%m%d_%H%M")
    if desktop.is_dir():
        return desktop / f"IELTS_Listening_Error_Notebook_{stamp}.docx"
    return plan_path.with_suffix(".docx")


def create(plan: dict[str, Any], output: Path) -> None:
    doc = SimpleDocx("IELTS Listening Error Notebook", "listening-error-review")
    doc.heading("IELTS Listening Error Notebook", 1)
    doc.paragraph(f"Source: {normalize_spaces(plan.get('source_title', 'IELTS Listening'))}")
    if plan.get("section_title"):
        doc.paragraph(f"Section: {normalize_spaces(plan['section_title'])}")
    if plan.get("summary"):
        doc.paragraph(plan["summary"])

    items = dicts(plan.get("items", []))
    rows = [
        [
            item.get("question_number", item.get("q", "")),
            item.get("user_answer", ""),
            item.get("correct_answer", ""),
            item.get("error_type", ""),
            item.get("replay_target", ""),
            item.get("micro_drill", ""),
        ]
        for item in items
    ] or [["", "", "", "", "", "No listening errors supplied."]]
    doc.heading("Error Map", 2)
    doc.table(["Q", "Your answer", "Correct", "Error type", "Replay target", "Micro-drill"], rows, [600, 1500, 1500, 1700, 2100, 1960])

    doc.page_break()
    doc.heading("Item Analysis", 1)
    for item in items:
        q = normalize_spaces(item.get("question_number", item.get("q", "")))
        doc.heading(f"Q{q}: {normalize_spaces(item.get('correct_answer', 'Listening item'))}", 2)
        for label, key in [
            ("Transcript / cue", "transcript"),
            ("Why it was missed", "cause"),
            ("Replay target", "replay_target"),
            ("Micro-drill", "micro_drill"),
        ]:
            if item.get(key):
                doc.paragraph(label, bold=True)
                doc.paragraph(item[key])

    review_plan = strings(plan.get("review_plan", []))
    if review_plan:
        doc.page_break()
        doc.heading("Review Plan", 1)
        for idx, item in enumerate(review_plan, start=1):
            doc.paragraph(f"{idx}. {item}")

    vocabulary = dicts(plan.get("vocabulary", []))
    if vocabulary:
        doc.heading("Useful Vocabulary", 2)
        doc.table(
            ["Phrase", "Meaning", "Source"],
            [[item.get("phrase", ""), item.get("meaning", ""), item.get("source_sentence", "")] for item in vocabulary],
            [2200, 2600, 4560],
        )

    if items:
        text = " ".join(str(item.get("transcript", "")) for item in items)
        if text:
            doc.paragraph(f"Transcript word count in reviewed snippets: {word_count(text)}", italic=True)
    doc.save(output)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan_json", type=Path)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--cleanup-plan", action="store_true")
    args = parser.parse_args()
    plan = json.loads(args.plan_json.read_text(encoding="utf-8"))
    output = args.output or default_output(args.plan_json)
    create(plan, output)
    if args.cleanup_plan:
        args.plan_json.unlink(missing_ok=True)
    print(output)


if __name__ == "__main__":
    main()

