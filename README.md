# IELTS Buddy 雅思学习 Skills

面向中国雅思学习者的公开 Skills 仓库。每个 Skill 都可单独安装；需要全面能力时一次安装全套。另提供可直接复制到 ChatGPT、DeepSeek 等网页 AI 的中文提示词。

> 本项目不代表 IELTS 官方机构。分数参考、批改和学习建议仅用于备考学习，不等同于官方成绩。

## 选择使用方式

| 你的情况 | 直接开始 |
| --- | --- |
| 使用 ChatGPT、DeepSeek 等网页 AI | [复制网页提示词](#网页-ai提示词) |
| 使用 Codex、Claude Code、Cursor、WorkBuddy 等本地 Agent | [安装一个或全部 Skills](#本地-agent-安装) |

## 网页 AI 提示词

打开所需场景，复制“完整提示词”到新对话；再按文档要求粘贴或上传材料。网页 AI 不会自动读取 IELTS Buddy 的题库、课程或学习记录。

- [万能雅思教练](网页版提示词/万能雅思教练.md)
- [学习计划](网页版提示词/学习计划.md)
- [作文批改](网页版提示词/作文批改.md)
- [口语陪练](网页版提示词/口语陪练.md)
- [阅读错题复盘](网页版提示词/阅读错题复盘.md)
- [听力错题复盘](网页版提示词/听力错题复盘.md)
- [词汇练习](网页版提示词/词汇练习.md)
- [模考复盘](网页版提示词/模考复盘.md)

首次使用可先看 [网页版提示词使用说明](网页版提示词/使用说明.md)。

## 本地 Agent 安装

需要 Node.js 18+。先查看可安装项：

```sh
npx skills@latest add Jobo16/ielts-all-in-one-skills --list
```

### 安装全套

将所有雅思学习 Skills 安装到 Codex 的用户级目录：

```sh
npx skills@latest add Jobo16/ielts-all-in-one-skills --skill '*' --agent codex --global --yes
```

安装后可直接说：

```text
根据我的目标推荐今天最该开始的一项雅思学习任务。
```

Agent 会按任务选择合适的已安装 Skill；也可以用下方名称明确触发。

### 安装一个 Skill

```sh
npx skills@latest add Jobo16/ielts-all-in-one-skills --skill ielts-writing-review --agent codex --global --yes
```

将 `ielts-writing-review` 替换为下表中的任意 Skill 名称。使用其他兼容 Agent 时，省略 `--agent codex` 进入交互式选择，或替换为对应 Agent 名称。

| Skill | 适用场景 | 触发示例 |
| --- | --- | --- |
| [`ielts-study-plan`](skills/ielts-study-plan) | 诊断、每日计划、周复盘、课程路线、资源推荐 | `使用 $ielts-study-plan 帮我安排今天的学习。` |
| [`ielts-writing-review`](skills/ielts-writing-review) | Academic Task 1/2 批改、二改、DOCX 批注 | `使用 $ielts-writing-review 批改这篇作文。` |
| [`ielts-speaking-coach`](skills/ielts-speaking-coach) | Part 1/2/3 陪练、话题素材、口语报告 | `使用 $ielts-speaking-coach 给我一题口语题。` |
| [`ielts-reading-review`](skills/ielts-reading-review) | 阅读错题、证据分析、阅读词汇手册 | `使用 $ielts-reading-review 复盘这些错题。` |
| [`ielts-listening-review`](skills/ielts-listening-review) | 听力错因、精听、错题本 | `使用 $ielts-listening-review 分析我的听力错题。` |
| [`ielts-vocabulary-coach`](skills/ielts-vocabulary-coach) | 主动回忆、搭配、词汇复习 | `使用 $ielts-vocabulary-coach 带我练 10 个词。` |
| [`ielts-mock-review`](skills/ielts-mock-review) | 模考成绩、失分模式、训练重点 | `使用 $ielts-mock-review 复盘这次模考。` |

### 复制给本地 Agent 的安装请求

打开对应场景，复制其中的“完整安装请求”给本地 Agent：

- [万能雅思教练](本地智能体安装提示词/万能雅思教练.md)
- [学习计划](本地智能体安装提示词/学习计划.md)
- [作文批改](本地智能体安装提示词/作文批改.md)
- [口语陪练](本地智能体安装提示词/口语陪练.md)
- [阅读错题复盘](本地智能体安装提示词/阅读错题复盘.md)
- [听力错题复盘](本地智能体安装提示词/听力错题复盘.md)
- [词汇练习](本地智能体安装提示词/词汇练习.md)
- [模考复盘](本地智能体安装提示词/模考复盘.md)

## 可选 IELTS Buddy 服务

已连接 OAuth MCP 的 Agent 可读取题库、课程、词汇、练习进度和学习记录：

```text
name: ielts-buddy
url: https://ieltsbuddy.igocn.cn/mcp
transport: streamable HTTP
auth: OAuth
```

没有 MCP 时，各 Skill 仍可基于用户主动提供的作文、题目、答案、文章、听力原文、词表、成绩或转写完成本地学习工作流。不要要求用户提供密码、API Key、访问令牌、浏览器 cookie 或无关本地文件。

## 仓库边界

- 仅保存可公开分发的 Skills、脚本、引用资料和验证工具。
- 可能在本地生成 DOCX 学习报告；学习镜像只作离线队列和缓存。
- 不包含 IELTS Buddy 应用源码、私有用户数据、题库内容、课程内容、模型密钥或完整官方评分标准。
- 写作批改工作流改编自 MIT 许可来源，许可说明见 [ielts-writing-review-skills.txt](skills/ielts-writing-review/licenses/ielts-writing-review-skills.txt) 与 [third-party-skill-sources.txt](skills/ielts-writing-review/licenses/third-party-skill-sources.txt)。

## 验证

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
```

## 许可证

本仓库的 Skills 指令和工具代码使用 [MIT 许可证](LICENSE) 发布。
