# 雅思学习技能：IELTS Buddy 一体化技能库

面向中国雅思学习者的开源 AI 学习助手仓库。它把雅思备考规划、作文批改、单词练习、听力错题复盘、阅读证据分析、口语陪练、模考复盘和学习资源推荐整理成两种使用方式：网页版 AI 提示词和可安装的 `ielts-buddy` 本地智能助手技能。

不熟悉本地智能助手的用户，可以把中文提示词直接复制到 ChatGPT、DeepSeek 等网页 AI 中使用；熟悉 Codex、Claude Code、Cursor、WorkBuddy 或 SkillHub 的用户，可以安装完整技能，使用文件处理、学习记录和 IELTS Buddy 服务连接等进阶能力。

> 本项目非 IELTS 官方产品，不代表任何考试主办方；分数参考、批改和学习建议仅供备考学习使用，不等同于官方成绩。

## 选择适合你的使用方式

| 你的情况 | 推荐方式 | 从这里开始 |
| --- | --- | --- |
| 只会使用 ChatGPT、DeepSeek 等网页版 AI | 复制中文提示词，无需安装 | [网页版提示词使用说明](网页版提示词/使用说明.md) |
| 已经使用 Codex、Claude Code、Cursor、WorkBuddy 等本地智能助手 | 安装完整的 `ielts-buddy` 技能 | [本地智能助手一键安装](#本地智能助手一键安装) |

## 网页版 AI：复制提示词，无需安装

第一次使用，推荐从 [万能雅思教练](网页版提示词/万能雅思教练.md) 开始：

1. 打开文档，复制“完整提示词”代码框里的全部内容。
2. 在 ChatGPT、DeepSeek 或其他网页 AI 中新建对话并粘贴。
3. 发送后按照 AI 的提问回答；不知道的信息可以直接说“不知道”。

也可以直接选择具体场景：

- [制定学习计划](网页版提示词/学习计划.md)
- [作文批改](网页版提示词/作文批改.md)
- [口语陪练](网页版提示词/口语陪练.md)
- [阅读错题复盘](网页版提示词/阅读错题复盘.md)
- [听力错题复盘](网页版提示词/听力错题复盘.md)
- [词汇练习](网页版提示词/词汇练习.md)
- [模考复盘](网页版提示词/模考复盘.md)

网页版 AI 不会自动读取 IELTS Buddy 题库、历史记录或课程进度。需要分析的作文、题目、答案、听力原文和成绩，应由用户主动粘贴或上传。完整说明见 [网页版提示词使用说明](网页版提示词/使用说明.md)。

## 本地智能助手一键安装

安装学习者技能 `ielts-buddy`。需要 Node.js 18+；命令会把完整技能安装到 Codex 的用户级技能目录：

```sh
npx skills add Jobo16/ielts-all-in-one-skills --skill ielts-buddy --agent codex --global --yes
```

使用其他兼容本地智能助手时，可运行交互式安装并选择目标：

```sh
npx skills add Jobo16/ielts-all-in-one-skills --skill ielts-buddy
```

安装完成后，在新对话中输入：

```text
使用 $ielts-buddy 介绍你能提供的雅思学习能力，并根据我的目标推荐第一个动作。
```

### 让本地智能助手自动安装

把下面这段话直接发给 Codex、WorkBuddy、CodeBuddy 或其他能管理技能的本地智能助手：

```text
请从 https://github.com/Jobo16/ielts-all-in-one-skills 安装学习者技能 `ielts-buddy`。
优先使用你内置的技能安装器；如果没有，则执行：
npx skills add Jobo16/ielts-all-in-one-skills --skill ielts-buddy --global --yes
必须安装完整目录，不能只复制 SKILL.md。安装后验证技能名称为 `ielts-buddy`，并告诉我安装位置和下一轮如何触发。
```

WorkBuddy 也可以在“专家·技能·连接器 → 添加技能”中描述上述需求，让 WorkBuddy 查找或创建安装任务；如果使用本地技能包，请导入 GitHub Release 中的 `ielts-buddy-skill-*.tar.gz` 完整压缩包。

## 这个仓库适合谁

- 只会使用 ChatGPT、DeepSeek 等网页版 AI，希望复制提示词后直接开始的人。
- 正在自学雅思，希望用 AI 做长期学习规划的人。
- 想要中文雅思作文批改，并生成带真实 Word 批注的 `.docx` 文件的人。
- 想把阅读、听力、口语、词汇复盘沉淀成可保存学习报告的人。
- 想在 Codex、Claude Code、Cursor、WorkBuddy 或 SkillHub 里安装雅思学习技能的人。
- 想基于 IELTS Buddy 的 MCP、接口或网页数据做本地学习闭环的人。

## 包含的技能

| 技能 | 用途 |
| --- | --- |
| [`ielts-buddy`](skills/ielts-buddy) | 一体化雅思自学智能助手技能：学习路线、作文批改、单词卡、阅读、听力和口语复盘、网页跳转链接、本地 DOCX 报告、MCP 学习记录。 |

## 主要能力

| 模块 | 本地可做 | 需要 IELTS Buddy 服务或网页的部分 |
| --- | --- | --- |
| 雅思写作批改 | 写作第一部分和第二部分生成带 Word 批注、斜体改写、分数参考、中文反馈和范文的 DOCX | 可选同步到网页写作练习 |
| 写作二改 | 检查二改是否解决上次批注，生成二改报告 DOCX | 可选读取历史写作记录 |
| 雅思单词卡 | 根据单词数据做主动回忆、中文反馈、周复习表 DOCX | 词书进度、历史学过词、跨设备复习状态 |
| 雅思阅读复盘 | 根据文章、答案和证据生成阅读证据图 DOCX | 题库文章、题目、历史错题 |
| 阅读词汇手册 | 从阅读文章提取高价值词组，生成中文词汇手册 DOCX | 可选写入个人词汇本 |
| 雅思听力精听/错题 | 根据文本、错题和正确答案生成听力错题本 DOCX | 音频播放、题库听力材料、网页精听 |
| 雅思口语教练 | 根据文字回答或转写文本生成口语反馈报告 DOCX | 口语题库、历史练习记录 |
| 雅思全科路线 | 本地生成今日计划和课程路线学习手册 | 官方课程路线、进度、下一课链接 |
| 学习资源推荐 | 以 IELTS 备考为主，使用仓库内置的 IELTS 与通用英语资源库做推荐和一周计划 | 无需外部本地目录 |
| 网页练习 | 给出数据摘要和稳定网页链接 | 计时做题、音频播放、整套模考、课程内容 |

## 本地智能助手快速开始

安装或添加这个技能后，直接问：

```text
使用 $ielts-buddy 介绍这个雅思技能能做什么，给我 5 个入门用法，并帮我选择第一个学习动作。
```

也可以直接从这些任务开始：

```text
使用 $ielts-buddy 批改这篇雅思 Task 2 作文，并输出带 Word 批注的 DOCX。
```

```text
使用 $ielts-buddy 给我今天 10 个雅思单词卡，不要重复我已经学过的词。
```

```text
使用 $ielts-buddy 把我的阅读错题整理成证据图 DOCX。
```

```text
使用 $ielts-buddy 根据这段听力文本和错题生成听力错题本。
```

更多入门说明见：

- [新手引导](skills/ielts-buddy/references/getting-started.md)
- [效果示例](skills/ielts-buddy/references/example-gallery.md)

## 可选 MCP 服务

部分能力需要连接 IELTS Buddy 外部服务：

```text
name: ielts-buddy
url: https://ieltsbuddy.igocn.cn/mcp
transport: streamable HTTP
auth: OAuth
```

服务用于读取或写入：

- 题库与练习入口；
- 雅思全科课程路线；
- 学习事件和练习历史；
- 词汇进度与历史学过的单词；
- browser-first 工具的数据摘要和跳转链接。

OAuth 由用户的 MCP 客户端或浏览器授权流程处理。本技能不会要求用户粘贴密码、API Key、客户端密钥、访问令牌、刷新令牌、私钥、浏览器 cookie 或无关本地文件。

如果没有配置 MCP，本技能仍然可以基于用户主动提供的作文、DOCX、阅读文章、听力文本、答案、单词或学习目标生成本地复盘和 DOCX 学习报告。

当前本地写作 Task 1 批改覆盖 IELTS Academic 图表、表格、地图和流程题；General Training Task 1 信件暂不在此工作流范围内。

客户端配置见 [MCP 配置说明](skills/ielts-buddy/references/setup.md)。

## 安全与数据使用

- 只读取用户主动提供或明确放入任务范围的作文、DOCX、阅读材料、听力文本、答案和学习偏好。
- 可能在本地创建 DOCX 报告。
- 可能在 `~/.ielts-buddy` 下维护本地 SQLite 学习镜像和离线队列。
- 用户授权 MCP 后，可能把学习事件、词汇复习结果或练习请求发送到 IELTS Buddy 服务。
- 不包含 IELTS Buddy 应用源码、私有用户数据、题库数据、课程内容、第三方练习素材、完整官方评分标准文本或模型密钥。

## 仓库边界

这个仓库只保存可公开分发的技能指令、脚本、引用资料和验证工具。

写作批改工作流改编自 Aaron Liang 的 MIT 许可雅思写作批改技能，许可文件见 [ielts-writing-review-skills.txt](skills/ielts-buddy/licenses/ielts-writing-review-skills.txt)。新的学习会话工作流参考了采用 MIT 许可的语言学习和文档类技能，来源说明见 [third-party-skill-sources.txt](skills/ielts-buddy/licenses/third-party-skill-sources.txt)。

IELTS Buddy 服务返回的材料和数据仍遵守其对应权利和条款。

## 验证

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
```

## 关键词

雅思 AI、雅思 Agent、雅思 Skill、IELTS Skills、IELTS Buddy、雅思作文批改、IELTS Writing Task 1、IELTS Writing Task 2、雅思小作文批改、雅思大作文批改、DOCX 批注、Word 批改、雅思单词卡、雅思词汇、雅思阅读复盘、雅思听力精听、雅思口语练习、MCP、Codex Skills、Claude Code Skills、Cursor、SkillHub、英语学习资源推荐。

## 许可证

本仓库的技能指令和工具代码使用 [MIT 许可证](LICENSE) 发布。
