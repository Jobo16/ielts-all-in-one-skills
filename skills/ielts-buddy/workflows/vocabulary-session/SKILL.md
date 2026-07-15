---
name: vocabulary-session
description: Run local IELTS vocabulary-card practice using server-prepared cards, per-word progress, active recall, immediate feedback, review write-back, and optional validated Weekly Vocabulary Sheet DOCX.
---

# Vocabulary Session

## Core Rule

Vocabulary practice is local-first and data-backed. The service prepares cards and stores progress; the Agent runs recall, hints, feedback, and session pacing.

## Start

1. Read `references/vocabulary.md`.
2. Choose source:
   - built-in wordbook: `core`, `listening`, or `reading`;
   - personal vocabulary book;
   - weak words from recent practice.
3. Call `ielts_vocabulary_prepare_cards` with a small limit, usually 5-10.
4. Avoid recent repeats with `excludeRecentlyReviewedDays` unless the user asks for due review.
5. Do not provide the web vocabulary-practice link unless the user explicitly asks for the web UI.

## Card Modes

Rotate modes to avoid passive recognition:

1. Recognition: English phrase to Chinese meaning.
2. Production: Chinese meaning or context to English phrase.
3. Cloze: fill the missing word in a sentence.
4. Collocation: choose or produce the natural partner word.
5. IELTS reuse: write one IELTS-style sentence.

Prefer production and cloze for words already seen before. Use recognition for new words.

## Per-Card Flow

1. Show one card only.
2. Ask for an answer before revealing the meaning.
3. If the answer is wrong or weak, give one hint before the full answer.
4. After the answer, give concise feedback:
   - correct form;
   - meaning in the current context;
   - one collocation or reusable chunk;
   - one common confusion if useful.
5. Record review with `ielts_vocabulary_record_review`:
   - `good`: correct without meaningful help;
   - `hard`: partly correct, slow, or needed a hint;
   - `again`: wrong after hint or unable to recall.

Batching the chat UI is acceptable, but never wait until the end to record outcomes if the client allows reliable writes per card.

## Session Summary

End with:

```text
本轮：<N> 个词
掌握：<words>
需要复习：<words>
下次优先：<wordbook/mode>
```

Do not inflate mastery from one correct answer. Use review history.

## Weekly Vocabulary Sheet

When the user asks for a weekly vocabulary review, printable sheet, or study report, deliver a validated Vocabulary Weekly Sheet `.docx`.

1. Read progress with `ielts_vocabulary_progress` and prepare representative words with `ielts_vocabulary_prepare_cards` if needed.
2. Build a weekly sheet plan.
3. Generate the DOCX with `scripts/create_vocabulary_weekly_sheet_docx.py`.
4. Validate it with `scripts/validate_vocabulary_weekly_sheet_docx.py`.
5. Return the absolute path to the final DOCX.

## Bundled Resources

- `scripts/create_vocabulary_weekly_sheet_docx.py`: create a vocabulary sheet with progress snapshot, word table, weak words, due reviews, and practice prompts.
- `scripts/validate_vocabulary_weekly_sheet_docx.py`: verify required sections, tables, Times New Roman, and plan content.

## JSON Weekly Sheet Plan

```json
{
  "week_title": "2026-07-14 Week",
  "wordbook": "IELTS Core",
  "summary": "Most weak words are academic verbs used in Reading passages.",
  "stats": {"reviewed": 24, "mastered": 8, "weak": 5},
  "words": [
    {
      "phrase": "contribute to",
      "meaning": "促成；有助于",
      "learning_state": "review",
      "last_rating": "hard",
      "next_review_at": "2026-07-15",
      "example": "Public transport can contribute to lower emissions."
    }
  ],
  "weak_words": [{"phrase": "whereas", "problem": "Meaning confused with where", "fix": "Use it for contrast."}],
  "due_reviews": [{"phrase": "contribute to", "due_at": "2026-07-15", "mode": "production"}],
  "practice_prompts": ["Use three weak words in one Task 2 body paragraph."]
}
```

```bash
python scripts/create_vocabulary_weekly_sheet_docx.py vocabulary_weekly_plan.json
python scripts/validate_vocabulary_weekly_sheet_docx.py ~/Desktop/IELTS_Vocabulary_Weekly_Sheet_YYYYMMDD_HHMM.docx --plan-json vocabulary_weekly_plan.json
```

## Borrowed Pattern

This workflow adapts MIT-licensed Fluent vocabulary-drill ideas: active recall, rotating prompt types, immediate feedback, and spaced-review write-back. IELTS Buddy replaces Fluent's local JSON databases with cloud-backed wordbook progress.
