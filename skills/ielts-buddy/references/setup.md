# Setup

IELTS Buddy exposes one OAuth-protected streamable HTTP MCP server:

```text
https://ieltsbuddy.igocn.cn/mcp
```

OAuth discovery and dynamic client registration are supported. Do not request a `client_id`, `client_secret`, access token, or refresh token from the user.

## Install The Skill

Clone the pinned release:

```sh
git clone --depth 1 --branch v0.1.0 https://github.com/Jobo16/ielts-skills.git
```

Install the complete `skills/ielts-buddy` directory, including `references` and `agents`.

## Codex

Install the Skill:

```sh
mkdir -p "$HOME/.codex/skills"
cp -R ielts-skills/skills/ielts-buddy "$HOME/.codex/skills/"
```

Add this to the Codex MCP configuration:

```toml
[mcp_servers.ielts-buddy]
url = "https://ieltsbuddy.igocn.cn/mcp"
```

Then authenticate:

```sh
codex mcp login ielts-buddy
```

## Claude Code

```sh
mkdir -p "$HOME/.claude/skills"
cp -R ielts-skills/skills/ielts-buddy "$HOME/.claude/skills/"
claude mcp add --scope user --transport http ielts-buddy "https://ieltsbuddy.igocn.cn/mcp"
claude mcp login ielts-buddy
```

## Other Clients

Create an MCP server named `ielts-buddy`, select streamable HTTP, use the URL above, and choose OAuth or browser authorization. Import this Skill as persistent agent guidance when the client supports `SKILL.md`; otherwise use its rules or custom-instruction mechanism.

## Troubleshooting

- `401` or an authorization prompt: complete MCP OAuth in the browser and retry.
- Missing tool: reconnect the MCP server, then inspect the live capability manifest.
- Missing scope: reauthorize so the client can request the capability's current scopes.
- Web-only capability: open the corresponding route from `web-workspace.md`.

When the user explicitly asks for IELTS Buddy data or an IELTS Buddy action, do not substitute a general web search while setup is incomplete. Explain that the remote step is paused, provide the appropriate setup command, and continue after the MCP connection is available.
