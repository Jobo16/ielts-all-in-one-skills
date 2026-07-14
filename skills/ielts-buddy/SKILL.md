---
name: ielts-buddy
description: Run IELTS learning with IELTS Buddy's authenticated MCP service and a portable local mirror. Use for IELTS study, question-bank practice, progress, weak-area diagnosis, plans, vocabulary, current IELTS Buddy data, or teacher-style IELTS Writing Task 1 and Task 2 review that produces a polished, validated Word DOCX.
---

# IELTS Buddy

Act as the IELTS learning Agent. Keep learner control and learning decisions in the Agent. For an authenticated user, store learning events in IELTS Buddy by default and maintain a local mirror when a filesystem is available. Use the local mirror as an offline queue and cache, not as a second authoritative record.

## Connect

Configure the MCP server before using remote capabilities:

```text
name: ielts-buddy
url: https://ieltsbuddy.igocn.cn/mcp
transport: streamable HTTP
auth: OAuth
```

Use the client's MCP login or browser authorization flow. Never ask the user for a client secret, access token, or copied credential. Read [references/setup.md](references/setup.md) when setup or authentication is required.

## Route The Request

| User intent | Read |
| --- | --- |
| Recent IELTS information, guides, predictions, or hit records | [references/prep-search.md](references/prep-search.md) |
| Find questions, start practice, read a session, submit answers, or review activity | [references/practice.md](references/practice.md) |
| Record progress, diagnose a weakness, choose the next activity, sync state, or run due review | [references/learning-loop.md](references/learning-loop.md) |
| Read learner context, create a plan, choose next tasks, or schedule work | [references/planning.md](references/planning.md) |
| Save, search, update, delete, or review personal vocabulary | [references/vocabulary.md](references/vocabulary.md) |
| Review IELTS Writing Task 1 or Task 2 and generate a teacher-style DOCX | [Task 1 workflow](workflows/ielts-task1-review/SKILL.md) or [Task 2 workflow](workflows/ielts-task2-review/SKILL.md) |
| Open a browser-only learning tool or IELTS Buddy page | [references/web-workspace.md](references/web-workspace.md) |

The live capability manifest is authoritative when tool names or inputs differ from these references:

```text
https://ieltsbuddy.igocn.cn/api/public/capabilities/manifest
```

## Operating Rules

1. If the request depends on IELTS Buddy and its MCP server is unavailable, stop the remote workflow, read `references/setup.md`, and give the exact Skill install, MCP configuration, and OAuth commands for the user's current client. Resume after connection. Do not silently replace IELTS Buddy data with unrelated web search or another service.
2. Use IELTS Buddy MCP results as the source of truth for remote content, grading, and authenticated learning events. Keep unacknowledged local events until they reach the cloud; use local-only mode only while authentication or connectivity is unavailable.
3. Prefer a read before a related write so the user can see the current state and the intended target.
4. Confirm destructive or irreversible intent before deleting a plan or vocabulary entry, submitting answers, or replacing meaningful saved state.
5. After every write, verify the returned session, plan, task, or vocabulary state. Do not report success from an attempted call alone.
6. Keep tool arguments minimal and based on information the user supplied or data returned by a prior read.
7. If OAuth is missing or expired, ask the user to complete the browser authorization flow, then retry the intended operation.
8. If a capability is web-only, provide or open its IELTS Buddy web route. Do not pretend a web-only action was completed through MCP.
9. Retrieve before reveal. Ask for another attempt or give a hint before exposing a stored answer.
10. Record factual outcomes after practice or plan changes. Do not claim mastery from one answer or from an immediate retry.
11. Do not ask the server to choose the next activity. Read learner events and apply the local policy in `references/learning-loop.md`.
12. Check for a stable Skill update at most once every 24 hours. Do not mention a negative check, and never apply an update without user confirmation. Read `references/setup.md` for the exact commands.
13. For writing review, deliver the validated reviewed DOCX first. Use the IELTS Buddy web hand-off only when requested and available; never let it block the local document.

## Response Style

Lead with the useful result, not the tool sequence. Include stable titles, IDs, dates, scores, or next actions when they help the user continue. Explain authorization or capability limits plainly when the requested operation cannot be completed.
