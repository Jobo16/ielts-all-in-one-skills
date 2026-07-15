# IELTS Skills

Free and open-source Agent Skills for using IELTS Buddy from Codex, Claude Code, Cursor, WorkBuddy, and other MCP-compatible clients.

This repository contains a portable IELTS learning Skill and a zero-dependency local learning mirror. IELTS Buddy provides the live question bank, preparation information, grading, cloud learning-event storage, OAuth, and MCP runtime at [ieltsbuddy.igocn.cn](https://ieltsbuddy.igocn.cn).

## Available Skill

| Skill | Purpose |
| --- | --- |
| [`ielts-buddy`](skills/ielts-buddy) | Run IELTS learning through IELTS Buddy, use local-first learning workflows, provide data plus links for browser-first tools, and generate polished IELTS DOCX artifacts locally. |

## First Run

After adding the Skill through your host client or SkillHub, ask:

```text
使用 $ielts-buddy 介绍这个雅思 Skill 能做什么，给我 5 个入门用法，并帮我选择第一个学习动作。
```

The first-run guide is bundled in [`getting-started.md`](skills/ielts-buddy/references/getting-started.md), and the output examples are listed in [`example-gallery.md`](skills/ielts-buddy/references/example-gallery.md).

## External Service Disclosure

Some capabilities require the external IELTS Buddy service:

```text
name: ielts-buddy
url: https://ieltsbuddy.igocn.cn/mcp
transport: streamable HTTP
auth: OAuth
```

The service is used for authenticated learning progress, question-bank metadata, course-route data, vocabulary progress, practice history, and browser-first learning links. OAuth is handled by the user's MCP client or browser authorization flow. The Skill must never ask the user to paste passwords, API keys, client secrets, access tokens, refresh tokens, private keys, or browser cookies.

When the MCP service is not configured, the Skill can still run local workflows from user-provided essays, reading passages, transcripts, answers, vocabulary notes, and bundled resource lists.

Client-specific MCP setup is documented in [`references/setup.md`](skills/ielts-buddy/references/setup.md).

## Safety And Data Use

- This Skill may read user-provided IELTS essays, DOCX files, reading materials, listening transcripts, answers, and study preferences when the user asks it to review or generate learning artifacts.
- This Skill may create local DOCX reports and a local SQLite learning mirror under `~/.ielts-buddy` unless the user configures another local data directory.
- This Skill may send authenticated learning events, vocabulary review results, or practice-related requests to the IELTS Buddy MCP service after the user authorizes that service.
- This Skill does not need and must not request passwords, private keys, API keys, client secrets, access tokens, browser cookies, or unrelated local files.
- 本 Skill 非 IELTS 官方产品，不代表任何考试主办方；分数参考、批改和学习建议仅供备考学习使用，不等同于官方成绩。

## What It Can Use

- Current IELTS preparation guides and published prep records.
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

This repository does not contain IELTS Buddy application code, private learner data, question-bank data, course content, third-party practice assets, full official descriptor text, external package replacement code, or model credentials. It includes a developer-maintained external learning-resource catalog for recommendation workflows. The bundled writing-review workflows adapt Aaron Liang's MIT-licensed IELTS writing review Skills; the license is included at [`skills/ielts-buddy/licenses/ielts-writing-review-skills.txt`](skills/ielts-buddy/licenses/ielts-writing-review-skills.txt). The newer learning-session workflows adapt ideas from MIT-licensed language-learning and document Skills; source notices are included at [`skills/ielts-buddy/licenses/third-party-skill-sources.txt`](skills/ielts-buddy/licenses/third-party-skill-sources.txt). Authenticated learning events are stored by IELTS Buddy; `~/.ielts-buddy/learning.db` is the local mirror and offline outbox.

## Validate

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
```

## License

The Skill instructions and repository tooling are released under the [MIT License](LICENSE). IELTS materials and data returned by the hosted service remain subject to their respective rights and terms.

## 中文说明

这是 IELTS Buddy 的免费开源 Agent Skill。本地 Agent 和网页 Agent 使用相同学习模型；登录后学习记录默认保存到云端，本地 SQLite 只作为镜像和离线队列。题库、课程和部分学习进度能力由 IELTS Buddy 服务提供。用户未授权连接 MCP 服务时，Skill 仍可基于用户主动提供的作文、文本、答案或学习材料生成本地复盘和 DOCX 学习报告。

本 Skill 非 IELTS 官方产品，不代表任何考试主办方；分数、批改和学习建议仅供备考参考，不等同于官方成绩。
