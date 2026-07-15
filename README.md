# IELTS Skills

Free and open-source Agent Skills for using IELTS Buddy from Codex, Claude Code, Cursor, WorkBuddy, and other MCP-compatible clients.

This repository contains a portable IELTS learning Skill and a zero-dependency local learning mirror. IELTS Buddy provides the live question bank, preparation information, grading, cloud learning-event storage, OAuth, and MCP runtime at [ieltsbuddy.igocn.cn](https://ieltsbuddy.igocn.cn).

## Available Skill

| Skill | Purpose |
| --- | --- |
| [`ielts-buddy`](skills/ielts-buddy) | Run IELTS learning through IELTS Buddy, use local-first learning workflows, provide data plus links for browser-first tools, and generate polished IELTS DOCX artifacts locally. |

## First Run

After installing the Skill, ask:

```text
Use $ielts-buddy to show me what this IELTS Skill can do, give me 5 starter prompts, and help me choose my first study action.
```

The first-run guide is bundled in [`getting-started.md`](skills/ielts-buddy/references/getting-started.md), and the output examples are listed in [`example-gallery.md`](skills/ielts-buddy/references/example-gallery.md).

## Install

Clone a stable release and copy the Skill into your Agent's skill directory:

```sh
git clone --depth 1 --branch v0.2.0 https://github.com/Jobo16/ielts-skills.git
```

Codex:

```sh
python3 ielts-skills/skills/ielts-buddy/scripts/update_skill.py install \
  --source ielts-skills/skills/ielts-buddy \
  --target "$HOME/.codex/skills/ielts-buddy"
```

Claude Code:

```sh
python3 ielts-skills/skills/ielts-buddy/scripts/update_skill.py install \
  --source ielts-skills/skills/ielts-buddy \
  --target "$HOME/.claude/skills/ielts-buddy"
```

Then configure the MCP server:

```text
name: ielts-buddy
url: https://ieltsbuddy.igocn.cn/mcp
transport: streamable HTTP
auth: OAuth
```

Client-specific setup is documented in [`references/setup.md`](skills/ielts-buddy/references/setup.md).

Check and apply stable updates from an installed Skill:

```sh
python3 <installed-skill>/scripts/update_skill.py check
python3 <installed-skill>/scripts/update_skill.py apply
```

`check` is silent at the Agent level when no update exists. `apply` should run only after user confirmation.

## What It Can Use

- Current IELTS preparation guides and prediction-hit records.
- Listening, reading, speaking, and writing question-bank search.
- Data plus browser links for course routes, practice, mock tests, listening dictation, and vocabulary practice.
- MCP-backed practice discovery, session launch, activity history, and supported browser-first tool data when configured.
- Cloud-backed learner events, explainable mastery, weak-area selection, and spaced review.
- A local mirror and offline outbox for uninterrupted learning.
- Learner profiles, footprints, weak points, and recent activity.
- Exam-prep planning, next actions, and scheduled study tasks.
- External learning-resource recommendations from the bundled developer-maintained catalog, with a validated recommendation DOCX when useful.
- Local daily-study sessions that combine due review, course-route progress, vocabulary, and practice links without letting the server choose the teaching policy; can produce a validated course-route workbook DOCX.
- Local vocabulary-card sessions using server-prepared cards, per-word progress, active recall, feedback, review write-back, and a validated weekly vocabulary sheet DOCX.
- Reading review with a validated Evidence Map DOCX when the Agent has passage/practice data, user answers, and answer evidence.
- Listening review with a validated Error Notebook DOCX when the Agent has dictation/practice results, transcript snippets, or answer data.
- Speaking review with a validated Speaking Report DOCX when the Agent has typed answers, transcripts, or speaking-topic data.
- Teacher-style IELTS Writing Task 1 and Task 2 review with anchored comments, rewrites, scores, feedback, a model answer, and validated DOCX output.
- Writing revision follow-up with a validated revision-report DOCX that checks whether the learner fixed earlier comments before giving a new score estimate.
- IELTS Reading passage lexicon extraction with anchored phrase comments, bilingual learner notes, examples, review prompts, and validated DOCX output.
- A visible-workflow catalog for current and future DOCX/report outputs such as writing reviews, reading maps, listening notebooks, speaking reports, vocabulary sheets, route workbooks, and weekly study reports.
- IELTS Buddy web experiences for courses, mock tests, practice, and learning tools through stable deep links.

The live capability contract is published at:

```text
https://ieltsbuddy.igocn.cn/api/public/capabilities/manifest
```

## Repository Boundary

This repository does not contain IELTS Buddy application code, private learner data, question-bank data, course content, third-party practice assets, full official descriptor text, or model credentials. It includes a developer-maintained external learning-resource catalog for recommendation workflows. The bundled writing-review workflows adapt Aaron Liang's MIT-licensed IELTS writing review Skills; the license is included at [`skills/ielts-buddy/licenses/ielts-writing-review-skills.txt`](skills/ielts-buddy/licenses/ielts-writing-review-skills.txt). The newer learning-session workflows adapt ideas from MIT-licensed language-learning and document Skills; source notices are included at [`skills/ielts-buddy/licenses/third-party-skill-sources.txt`](skills/ielts-buddy/licenses/third-party-skill-sources.txt). Authenticated learning events are stored by IELTS Buddy; `~/.ielts-buddy/learning.db` is the local mirror and offline outbox.

## Validate

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
```

## License

The Skill instructions and repository tooling are released under the [MIT License](LICENSE). IELTS materials and data returned by the hosted service remain subject to their respective rights and terms.

## 中文说明

这是 IELTS Buddy 的免费开源 Agent Skill。本地 Agent 和网页 Agent 使用相同学习模型；登录后学习记录默认保存到云端，本地 SQLite 只作为镜像和离线队列。题库、课程和批改能力由 IELTS Buddy 服务提供。
