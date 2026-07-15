# Visual Workflow Catalog

Visible workflows are high-value because the user receives an artifact that looks like teacher work, not just chat. Prefer DOCX when comments, rewrites, tables, or printable handouts matter. Prefer browser links only when the interaction itself is browser-owned.

## Implemented

| Workflow | Input | Output | Value |
| --- | --- | --- | --- |
| Writing Task 1 review | DOCX with prompt image and answer, or pasted answer plus image | Reviewed DOCX with anchored comments, italic rewrites, scores, feedback, and model answer | Strongest visual proof of teacher-style marking. |
| Writing Task 2 review | DOCX or pasted prompt and essay | Reviewed DOCX with anchored comments, rewrites, scores, feedback, and model essay | Core IELTS writing correction product. |
| Writing revision loop | Reviewed DOCX or original review notes plus revised answer | Revision-report DOCX with fix-check table, score movement, new issues, revised answer, next rewrite target, and micro-drills | Converts first-pass correction into an actual rewrite loop. |
| Reading answer evidence map | Practice data, user answers, or a passage DOCX | Evidence-map DOCX with answer table, evidence sentence, paraphrase bridge, trap explanation, error type, and micro-drills | Turns wrong answers into reusable Reading strategy evidence. |
| Reading lexicon | Reading passage DOCX | Annotated DOCX with phrase comments, bilingual notes, examples, and review prompts | Turns reading materials into reusable vocabulary learning. |
| Listening error notebook | Browser dictation/practice result, transcript, or pasted answer/transcript | Error-notebook DOCX with answer map, replay targets, transcript snippets, error causes, micro-drills, and vocabulary | Converts browser-first listening attempts into repeatable local review. |
| Speaking interview report | Typed answers, transcript, or speaking-topic-weaver data | Speaking report DOCX with criterion scores, answer review, natural rewrites, reusable chunks, recurring patterns, and next questions | Makes typed/transcribed speaking practice reusable without ASR dependency. |
| Vocabulary review sheet | Vocabulary progress, prepared cards, and review results | Weekly vocabulary sheet DOCX with progress snapshot, word table, weak words, due reviews, and practice prompts | Gives local Agent memory of what not to repeat and what is due next. |
| Course-route workbook | Course route data, route progress, and next actions | Course route workbook DOCX with next actions, route checklist, success criteria, and checkpoints | Converts the full-course route into a self-study artifact. |

## Next Workflows To Build

| Workflow | Data source | Local Skill rule | Visible output |
| --- | --- | --- | --- |
| Weekly study report | Learning events, route progress, vocabulary progress | Summarize evidence, weak patterns, due review, and the next three actions | One-page IELTS progress report DOCX/PDF. |

## Design Criteria

Build a workflow only when at least one is true:

- the output benefits from anchored comments, tables, page breaks, or printability;
- the user can compare before/after visually;
- the artifact can be saved and reused across sessions;
- the workflow converts browser or service data into local learning material.

Do not generate a DOCX merely to decorate a short answer. Plain chat is better for simple next actions, small explanations, or a single vocabulary drill.

## Implementation Order

1. Weekly study report: summarize cross-skill evidence, weak patterns, due review, and next three actions.
2. Optional DOCX polish pass: add richer styling or anchored source comments where they materially improve usability.
