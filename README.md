# IELTS Skills

Free and open-source Agent Skills for using IELTS Buddy from Codex, Claude Code, Cursor, WorkBuddy, and other MCP-compatible clients.

This repository contains a portable IELTS learning Skill and a zero-dependency local learning store. IELTS Buddy provides the live question bank, preparation information, grading, optional cloud event sync, OAuth, and MCP runtime at [ieltsbuddy.igocn.cn](https://ieltsbuddy.igocn.cn).

## Available Skill

| Skill | Purpose |
| --- | --- |
| [`ielts-buddy`](skills/ielts-buddy) | Route IELTS requests to IELTS Buddy MCP tools and web capabilities, with OAuth, write confirmation, and result verification rules. |

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
- Practice session creation, reading, answer submission, and activity history.
- Local learner events, explainable mastery, weak-area selection, and spaced review.
- Optional cloud backup and cross-device synchronization of learning events.
- Learner profiles, footprints, weak points, and recent activity.
- Exam-prep planning, next actions, and scheduled study tasks.
- IELTS Buddy web experiences for courses, mock tests, practice, and learning tools.

The live capability contract is published at:

```text
https://ieltsbuddy.igocn.cn/api/public/capabilities/manifest
```

## Repository Boundary

This repository does not contain IELTS Buddy application code, private learner data, question-bank data, course content, model credentials, or third-party Skill snapshots. Learner data stays in `~/.ielts-buddy/learning.db` unless the user connects IELTS Buddy and syncs it.

## Validate

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
```

## License

The Skill instructions and repository tooling are released under the [MIT License](LICENSE). IELTS materials and data returned by the hosted service remain subject to their respective rights and terms.

## 中文说明

这是 IELTS Buddy 的免费开源 Agent Skill。本地 Agent 和网页 Agent 使用相同学习模型；本地记录默认保存在用户电脑，云端同步可选。题库、课程和批改能力由 IELTS Buddy 服务提供。
