# Setup

IELTS Buddy exposes one OAuth-protected streamable HTTP MCP server:

```text
https://ieltsbuddy.igocn.cn/mcp
```

OAuth discovery and dynamic client registration are supported. Do not request a `client_id`, `client_secret`, access token, or refresh token from the user.

## Install The Skill

Clone the pinned release:

```sh
git clone --depth 1 --branch v0.2.0 https://github.com/Jobo16/ielts-skills.git
```

Install the complete `skills/ielts-buddy` directory with the bundled installer. It records the installed version outside the Skill directory and initializes the local learning database.

## Codex

Install the Skill:

```sh
python3 ielts-skills/skills/ielts-buddy/scripts/update_skill.py install \
  --source ielts-skills/skills/ielts-buddy \
  --target "$HOME/.codex/skills/ielts-buddy"
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
python3 ielts-skills/skills/ielts-buddy/scripts/update_skill.py install \
  --source ielts-skills/skills/ielts-buddy \
  --target "$HOME/.claude/skills/ielts-buddy"
claude mcp add --scope user --transport http ielts-buddy "https://ieltsbuddy.igocn.cn/mcp"
claude mcp login ielts-buddy
```

## Update

Check at most once every 24 hours unless the user explicitly asks to refresh:

```sh
python3 <installed-skill>/scripts/update_skill.py check
```

When `updateAvailable=true`, summarize the version change and ask for confirmation. After confirmation:

```sh
python3 <installed-skill>/scripts/update_skill.py apply
```

Never run `apply` automatically. The updater accepts only stable semantic versions, downloads over HTTPS, verifies the service-provided SHA-256, validates the package, and atomically replaces the Skill. Learning data remains under `~/.ielts-buddy`.

If `supported=false`, pause remote write operations until the Skill is updated. If `packageReady=false`, do not bypass the updater or install from `main`; explain that the stable release package is not available yet.

## Other Clients

Create an MCP server named `ielts-buddy`, select streamable HTTP, use the URL above, and choose OAuth or browser authorization. Import this Skill as persistent agent guidance when the client supports `SKILL.md`; otherwise use its rules or custom-instruction mechanism.

## Troubleshooting

- `401` or an authorization prompt: complete MCP OAuth in the browser and retry.
- Missing tool: reconnect the MCP server, then inspect the live capability manifest.
- Missing scope: reauthorize so the client can request the capability's current scopes.
- Web-only capability: open the corresponding route from `web-workspace.md`.

When the user explicitly asks for IELTS Buddy data or an IELTS Buddy action, do not substitute a general web search while setup is incomplete. Explain that the remote step is paused, provide the appropriate setup command, and continue after the MCP connection is available.
