# MCP 配置说明

这份说明只用于在用户已经通过客户端或 SkillHub 添加 Skill 后，配置可选的 IELTS Buddy MCP 服务。本 Skill 本身包含运行时指导和本地学习工作流脚本，不依赖自更新或安装脚本。

## 外部服务

IELTS Buddy 暴露一个 OAuth 保护的 streamable HTTP MCP 服务：

```text
https://ieltsbuddy.igocn.cn/mcp
```

支持 OAuth discovery 和动态客户端注册。不要向用户索要 `client_id`、`client_secret`、access token、refresh token、密码、API Key、私钥或浏览器 cookie。

## 哪些能力需要 MCP

以下能力使用 MCP 服务：

- 登录后的学习事件和云端进度；
- 雅思全科课程路线和路线进度；
- 题库元数据和练习历史；
- 词书进度、历史学过单词和复习写回；
- 练习、模考、听力播放和网页学习工具的 browser-first 链接。

没有 MCP 时，继续基于用户提供的作文、DOCX、阅读文章、听力文本、答案和学习偏好运行本地工作流。

## Codex 配置

把下面配置加入 Codex MCP 配置：

```toml
[mcp_servers.ielts-buddy]
url = "https://ieltsbuddy.igocn.cn/mcp"
```

然后通过客户端登录：

```sh
codex mcp login ielts-buddy
```

## Claude Code 配置

```sh
claude mcp add --scope user --transport http ielts-buddy "https://ieltsbuddy.igocn.cn/mcp"
claude mcp login ielts-buddy
```

## 其他客户端

创建一个名为 `ielts-buddy` 的 MCP server，选择 streamable HTTP，URL 使用上面的地址，并选择 OAuth 或浏览器授权。

## 排查

- `401` 或出现授权提示：在浏览器里完成 MCP OAuth，然后重试。
- 缺少 tool：重新连接 MCP server，再查看实时能力清单。
- 缺少 scope：重新授权，让客户端请求当前能力需要的 scope。
- Web-only 能力：打开 `web-workspace.md` 中对应的网页路线。

当用户明确要求 IELTS Buddy 数据或动作时，如果配置未完成，不要用普通网页搜索替代。说明远程步骤暂停，给出 MCP 配置或 OAuth 步骤，同时继续处理可本地完成的学习工作流。

## 安全说明

本 Skill 可能创建本地 DOCX 文件，并在用户未指定其他目录时维护 `~/.ielts-buddy` 下的 SQLite 学习镜像。它只应读取用户提供或明确放入任务范围的文件。不得请求或检查密码、私钥、API Key、client secret、access token、浏览器 cookie 或无关本地目录。

本 Skill 非 IELTS 官方产品，不代表任何考试主办方；分数参考、批改和学习建议仅供备考学习使用，不等同于官方成绩。
