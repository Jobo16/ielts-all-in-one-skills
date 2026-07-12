# IELTS Skills

Free and open-source Agent Skills for using IELTS Buddy from Codex, Claude Code, Cursor, WorkBuddy, and other MCP-compatible clients.

This repository contains portable instructions only. IELTS Buddy provides the live question bank, preparation information, practice sessions, learner state, study plans, OAuth, and MCP runtime at [ieltsbuddy.igocn.cn](https://ieltsbuddy.igocn.cn).

## Available Skill

| Skill | Purpose |
| --- | --- |
| [`ielts-buddy`](skills/ielts-buddy) | Route IELTS requests to IELTS Buddy MCP tools and web capabilities, with OAuth, write confirmation, and result verification rules. |

## Install

Clone a stable release and copy the Skill into your Agent's skill directory:

```sh
git clone --depth 1 --branch v0.1.0 https://github.com/Jobo16/ielts-skills.git
```

Codex:

```sh
mkdir -p "$HOME/.codex/skills"
cp -R ielts-skills/skills/ielts-buddy "$HOME/.codex/skills/"
```

Claude Code:

```sh
mkdir -p "$HOME/.claude/skills"
cp -R ielts-skills/skills/ielts-buddy "$HOME/.claude/skills/"
```

Then configure the MCP server:

```text
name: ielts-buddy
url: https://ieltsbuddy.igocn.cn/mcp
transport: streamable HTTP
auth: OAuth
```

Client-specific setup is documented in [`references/setup.md`](skills/ielts-buddy/references/setup.md).

## What It Can Use

- Current IELTS preparation guides and prediction-hit records.
- Listening, reading, speaking, and writing question-bank search.
- Practice session creation, reading, answer submission, and activity history.
- Learner profiles, footprints, weak points, and recent activity.
- Exam-prep planning, next actions, and scheduled study tasks.
- IELTS Buddy web experiences for courses, mock tests, practice, and learning tools.

The live capability contract is published at:

```text
https://ieltsbuddy.igocn.cn/api/public/capabilities/manifest
```

## Repository Boundary

This repository does not contain IELTS Buddy application code, private learner data, question-bank data, course content, model credentials, or third-party Skill snapshots. It only describes how an Agent should use the public IELTS Buddy service safely and predictably.

## Validate

```sh
python3 scripts/validate_skills.py
```

## License

The Skill instructions and repository tooling are released under the [MIT License](LICENSE). IELTS materials and data returned by the hosted service remain subject to their respective rights and terms.

## 中文说明

这是 IELTS Buddy 的免费开源 Agent Skill。Skill 本身只描述如何通过 MCP 和网页能力使用 IELTS Buddy，不包含题库、课程、用户数据或后端实现。不会使用 Skills 的用户仍可直接访问 [IELTS Buddy 网页版](https://ieltsbuddy.igocn.cn)。
