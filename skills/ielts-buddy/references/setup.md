# Setup

Use this guide only for configuring the optional IELTS Buddy MCP service after the Skill is already added through the user's host client or SkillHub. This Skill contains runtime guidance and local learning workflow scripts; it does not replace its own package.

## External Service

IELTS Buddy exposes one OAuth-protected streamable HTTP MCP server:

```text
https://ieltsbuddy.igocn.cn/mcp
```

OAuth discovery and dynamic client registration are supported. Do not request a `client_id`, `client_secret`, access token, refresh token, password, API key, private key, or browser cookie from the user.

## What Requires MCP

Use the MCP service for:

- authenticated learning events and cloud progress;
- course routes and route progress;
- question-bank metadata and practice history;
- vocabulary wordbook progress and review write-back;
- browser-first links for practice, mock tests, listening playback, and web learning tools.

Without MCP, continue with local workflows based on user-provided essays, DOCX files, reading passages, listening transcripts, answers, and study preferences.

## Codex MCP Configuration

Add this to the Codex MCP configuration:

```toml
[mcp_servers.ielts-buddy]
url = "https://ieltsbuddy.igocn.cn/mcp"
```

Then authenticate through the client:

```sh
codex mcp login ielts-buddy
```

## Claude Code MCP Configuration

```sh
claude mcp add --scope user --transport http ielts-buddy "https://ieltsbuddy.igocn.cn/mcp"
claude mcp login ielts-buddy
```

## Other Clients

Create an MCP server named `ielts-buddy`, select streamable HTTP, use the URL above, and choose OAuth or browser authorization.

## Troubleshooting

- `401` or an authorization prompt: complete MCP OAuth in the browser and retry.
- Missing tool: reconnect the MCP server, then inspect the live capability manifest.
- Missing scope: reauthorize so the client can request the capability's current scopes.
- Web-only capability: open the corresponding route from `web-workspace.md`.

When the user explicitly asks for IELTS Buddy data or an IELTS Buddy action, do not substitute a general web search while setup is incomplete. Explain that the remote step is paused, provide the appropriate MCP configuration or OAuth step, and continue with local workflows when possible.

## Safety Disclosure

This Skill may create local DOCX files and maintain a local SQLite learning mirror under `~/.ielts-buddy` unless the user configures another local data directory. It should read only files the user provides or explicitly places in scope. It must not request or inspect passwords, private keys, API keys, client secrets, access tokens, browser cookies, or unrelated local directories.

本 Skill 非 IELTS 官方产品，不代表任何考试主办方；分数参考、批改和学习建议仅供备考学习使用，不等同于官方成绩。
