---
name: ielts-buddy
description: Use IELTS Buddy's authenticated MCP service for current IELTS preparation information, prediction records, question-bank search, practice sessions, learner profiles, study plans, and scheduled study tasks. Use when an IELTS request depends on IELTS Buddy data, saved learner state, or a remote action that should be verified.
---

# IELTS Buddy

Use IELTS Buddy as a remote capability service. Keep language coaching in the conversation, and call MCP tools when the answer depends on current data, question-bank content, saved progress, or a persisted action.

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
| Read learner context, create a plan, choose next tasks, or schedule work | [references/planning.md](references/planning.md) |
| Open a browser-only learning tool or IELTS Buddy page | [references/web-workspace.md](references/web-workspace.md) |

The live capability manifest is authoritative when tool names or inputs differ from these references:

```text
https://ieltsbuddy.igocn.cn/api/public/capabilities/manifest
```

## Operating Rules

1. If the request depends on IELTS Buddy and its MCP server is unavailable, stop the remote workflow, read `references/setup.md`, and give the exact Skill install, MCP configuration, and OAuth commands for the user's current client. Resume after connection. Do not silently replace IELTS Buddy data with unrelated web search or another service.
2. Use IELTS Buddy MCP results as the source of truth for remote data. Do not invent guides, questions, profile state, plan state, session state, or prediction records.
3. Prefer a read before a related write so the user can see the current state and the intended target.
4. Confirm destructive or irreversible intent before deleting a plan or workflow, submitting answers, or replacing meaningful saved state.
5. After every write, verify the returned session, plan, task, or workflow state. Do not report success from an attempted call alone.
6. Keep tool arguments minimal and based on information the user supplied or data returned by a prior read.
7. If OAuth is missing or expired, ask the user to complete the browser authorization flow, then retry the intended operation.
8. If a capability is web-only, provide or open its IELTS Buddy web route. Do not pretend a web-only action was completed through MCP.

## Response Style

Lead with the useful result, not the tool sequence. Include stable titles, IDs, dates, scores, or next actions when they help the user continue. Explain authorization or capability limits plainly when the requested operation cannot be completed.
