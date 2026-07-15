# Getting Started

Use this guide when the learner asks how to use IELTS Buddy, what the Skill can do, or how to start after adding it.
Answer new Chinese IELTS learners in Simplified Chinese by default.

## What This Skill Does

IELTS Buddy turns the local Agent into an IELTS study coach. It can combine IELTS Buddy service data, local learning rules, and local DOCX workflows to plan study, review practice, run vocabulary sessions, and produce teacher-style artifacts.

## First Check

Before starting, identify which mode is available:

- Logged in with IELTS Buddy MCP: use route progress, question-bank data, vocabulary progress, practice history, and cloud learning events.
- No MCP yet: still run local workflows from user-provided essays, transcripts, reading passages, answers, or the bundled learning-resource catalog.
- Browser-first task: provide both the best available data summary and the IELTS Buddy deep link.

If the user is new, ask for only one missing choice: target band, exam date, weakest skill, or whether they want a visible DOCX result.

## Starter Prompts

Offer these prompts directly:

1. `使用 $ielts-buddy 看看我接下来雅思自学该做什么。`
2. `使用 $ielts-buddy 给我做一个冲 Band 7.0 的 7 天雅思计划。`
3. `使用 $ielts-buddy 给我今天 10 个单词卡，不要重复我已经学过的词。`
4. `使用 $ielts-buddy 推荐适合 B1-B2 雅思学习者的听力资源。`
5. `使用 $ielts-buddy 说明哪些功能需要网页，哪些可以本地完成。`

## Quick Wins

- Writing review: ask the learner to paste a Task 1/Task 2 answer or attach a DOCX. Output a reviewed DOCX.
- Vocabulary: ask for level, wordbook, or target topic. Output active-recall cards and record review results when storage is available.
- Reading review: ask for passage, answer key, user answers, and evidence if not available from IELTS Buddy. Output an evidence map.
- Listening review: ask for transcript snippets, user answer, and correct answer. Output an error notebook.
- Study route: if logged in, read the route and progress; otherwise create a local plan and provide web links.

## Common Limits

- Question-bank content, course lessons, audio playback, timed mock tests, and durable cross-device progress require IELTS Buddy service data or browser links.
- The public Skill does not bundle third-party practice materials, course content, or full official descriptor text.
- Local DOCX workflows need enough input material. Do not invent missing passages, transcripts, answer keys, charts, or prompts.
- If OAuth or MCP is unavailable, give setup instructions from `setup.md` and continue with local workflows where possible.

## Good First Response

When a user asks “how do I use this?”, answer with:

1. one-sentence purpose;
2. whether login/MCP is connected if known;
3. five starter prompts;
4. one recommended first action based on their goal;
5. a note that visible DOCX workflows are available for writing, reading, listening, speaking, vocabulary, and study-route reports.
