---
name: speaking-coach
description: Coach IELTS Speaking from typed answers, transcripts, or IELTS Buddy speaking-topic data with communication-first feedback, concise corrections, reusable chunks, progress recording, and a validated Speaking Report DOCX.
---

# Speaking Coach

## Core Rule

Speaking feedback should protect fluency. Correct the problems that affect IELTS performance, not every minor slip.

## Inputs

Use:

- user-typed answers;
- pasted transcript;
- IELTS Buddy speaking topic/material data;
- the user's target band and part number.

If audio or ASR is unavailable, run typed speaking practice. Do not pretend to assess pronunciation from text.

## Practice Flow

1. Pick IELTS Speaking Part 1, 2, or 3.
2. Ask one question at a time.
3. Let the user answer fully before correcting.
4. Evaluate in this order:
   - task relevance and idea development;
   - fluency and coherence;
   - lexical resource;
   - grammar range and accuracy;
   - pronunciation only when audio evidence exists.
5. Give a natural alternative answer or sentence upgrade.
6. Add 2-4 reusable chunks.
7. Ask one follow-up question.

## Feedback Format

Use a short structure:

```text
Score estimate: <band or range>
Strong: <one concrete point>
Fix first: <one or two issues>
Natural version: <rewritten answer or sentence>
Reusable chunks: <chunks>
Next question: <question>
```

Keep corrections to the top 3. Track recurring patterns across the session.

## Default Deliverable

Deliver a validated Speaking Report `.docx` by default for a full Part 2 answer, Part 3 answer set, transcript, or mock interview. For one quick Part 1 response, chat feedback is acceptable.

1. Build a speaking report plan from typed answers or transcript data.
2. Generate the DOCX with `scripts/create_speaking_report_docx.py`.
3. Validate it with `scripts/validate_speaking_report_docx.py`.
4. Return the absolute path to the final DOCX.
5. If validation fails, fix the plan and rerun generation plus validation.

## Bundled Resources

- `scripts/create_speaking_report_docx.py`: create a Speaking Report DOCX with criterion scores, answer review, natural rewrites, reusable chunks, recurring patterns, and next questions.
- `scripts/validate_speaking_report_docx.py`: verify required sections, Times New Roman, and plan content.

## JSON Speaking Report Plan

```json
{
  "session_title": "Part 2: Describe a useful website",
  "part": "Part 2",
  "band_estimate": "6.5",
  "overall_feedback": "The answer is clear, but examples need more development.",
  "criterion_scores": {
    "Fluency and Coherence": {"score": "6.5", "note": "Mostly clear but some repetition."},
    "Lexical Resource": {"score": "7", "note": "Good topic vocabulary."}
  },
  "answers": [
    {
      "question": "Describe a useful website.",
      "answer": "I often use a website for learning English...",
      "feedback": "The topic is relevant, but the second example is underdeveloped.",
      "natural_version": "I use this website almost every day because it gives me short, practical exercises.",
      "reusable_chunks": ["almost every day", "short, practical exercises"],
      "focus": "Extend one example with a result."
    }
  ],
  "recurring_patterns": ["Examples stop before the result."],
  "next_questions": ["How has this website changed your study habits?"]
}
```

```bash
python scripts/create_speaking_report_docx.py speaking_report_plan.json
python scripts/validate_speaking_report_docx.py ~/Desktop/IELTS_Speaking_Report_YYYYMMDD_HHMM.docx --plan-json speaking_report_plan.json
```

## Borrowed Pattern

This workflow adapts MIT-licensed English Coach and lang-tutor patterns: answer the real request first, keep corrections concise, detect recurring patterns, and separate conversation from language feedback.
