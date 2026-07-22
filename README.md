# 雅思学习 Skills：IELTS Buddy All-in-One Skills

面向中国雅思学习者的开源 AI Agent Skills 仓库。它把雅思备考规划、雅思作文批改 DOCX、Task 1 小作文批改、Task 2 大作文批改、雅思单词卡、听力精听错题本、阅读证据图、口语反馈报告和学习资源推荐整合到一个可安装的 `ielts-buddy` Skill 中。

适用于 Codex、Claude Code、Cursor、WorkBuddy、小红书 SkillHub 以及其他支持 Agent Skills / MCP 的本地 AI 助手。IELTS Buddy 服务提供题库、课程路线、学习记录、词汇进度、OAuth 和 MCP 能力；本仓库提供可独立运行的本地学习规则、DOCX 工作流和离线学习镜像。

> 本 Skill 非 IELTS 官方产品，不代表任何考试主办方；分数参考、批改和学习建议仅供备考学习使用，不等同于官方成绩。

## 一键安装

安装学习者 Skill `ielts-buddy`。需要 Node.js 18+；命令会把完整 Skill 安装到 Codex 的用户级 Skills 目录：

```sh
npx skills add Jobo16/ielts-all-in-one-skills --skill ielts-buddy --agent codex --global --yes
```

使用其他兼容 Agent 时，可运行交互式安装并选择目标 Agent：

```sh
npx skills add Jobo16/ielts-all-in-one-skills --skill ielts-buddy
```

安装完成后，在新的对话中输入：

```text
使用 $ielts-buddy 介绍你能提供的雅思学习能力，并根据我的目标推荐第一个动作。
```

### 让 Agent 自动安装

把下面这段话直接发给 Codex、WorkBuddy、CodeBuddy 或其他能管理 Agent Skills 的本地 Agent：

```text
请从 https://github.com/Jobo16/ielts-all-in-one-skills 安装学习者 Skill `ielts-buddy`。
优先使用你内置的 Skill 安装器；如果没有，则执行：
npx skills add Jobo16/ielts-all-in-one-skills --skill ielts-buddy --global --yes
必须安装完整目录，不能只复制 SKILL.md。安装后验证 Skill 名称为 `ielts-buddy`，并告诉我安装位置和下一轮如何触发。
```

WorkBuddy 也可以在“专家·技能·连接器 → 添加技能”中描述上述需求，让 WorkBuddy 查找或创建安装任务；如果使用本地技能包，请导入 GitHub Release 中的 `ielts-buddy-skill-*.tar.gz` 完整压缩包。

## 这个仓库适合谁

- 正在自学雅思，希望用 AI Agent 做长期学习规划的人。
- 想要中文雅思作文批改，并生成带真实 Word 批注的 `.docx` 文件的人。
- 想把阅读、听力、口语、词汇复盘沉淀成可保存学习报告的人。
- 想在 Codex、Claude Code、Cursor、WorkBuddy 或 SkillHub 里安装雅思学习 Skill 的人。
- 想基于 IELTS Buddy 的 MCP / API / Web 数据做本地 Agent 学习闭环的人。

## 包含的 Skill

| Skill | 用途 |
| --- | --- |
| [`ielts-buddy`](skills/ielts-buddy) | 雅思自学 All-in-One Agent Skill：学习路线、作文批改、单词卡、阅读/听力/口语复盘、网页跳转链接、本地 DOCX 报告、MCP 学习记录。 |

## 主要能力

| 模块 | 本地可做 | 需要 IELTS Buddy 服务或网页的部分 |
| --- | --- | --- |
| 雅思写作批改 | Task 1 / Task 2 生成带 Word 批注、斜体改写、分数参考、中文反馈和范文的 DOCX | 可选同步到网页写作练习 |
| 写作二改 | 检查二改是否解决上次批注，生成二改报告 DOCX | 可选读取历史写作记录 |
| 雅思单词卡 | 根据单词数据做主动回忆、中文反馈、周复习表 DOCX | 词书进度、历史学过词、跨设备复习状态 |
| 雅思阅读复盘 | 根据文章、答案和证据生成阅读证据图 DOCX | 题库文章、题目、历史错题 |
| 阅读词汇手册 | 从阅读文章提取高价值词组，生成中文词汇手册 DOCX | 可选写入个人词汇本 |
| 雅思听力精听/错题 | 根据文本、错题和正确答案生成听力错题本 DOCX | 音频播放、题库听力材料、网页精听 |
| 雅思口语教练 | 根据 typed answer 或 transcript 生成口语反馈报告 DOCX | 口语题库、历史练习记录 |
| 雅思全科路线 | 本地生成今日计划和课程路线学习手册 | 官方课程路线、进度、下一课链接 |
| 学习资源推荐 | 以 IELTS 备考为主，使用仓库内置的 IELTS 与通用英语资源库做推荐和一周计划 | 无需外部本地目录 |
| Browser-first 练习 | 给出数据摘要和稳定网页链接 | 计时做题、音频播放、整套模考、课程内容 |

## 快速开始

安装或添加这个 Skill 后，直接问：

```text
使用 $ielts-buddy 介绍这个雅思 Skill 能做什么，给我 5 个入门用法，并帮我选择第一个学习动作。
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

OAuth 由用户的 MCP 客户端或浏览器授权流程处理。这个 Skill 不会要求用户粘贴密码、API Key、client secret、access token、refresh token、私钥、浏览器 cookie 或无关本地文件。

如果没有配置 MCP，本 Skill 仍然可以基于用户主动提供的作文、DOCX、阅读文章、听力文本、答案、单词或学习目标生成本地复盘和 DOCX 学习报告。

当前本地写作 Task 1 批改覆盖 IELTS Academic 图表、表格、地图和流程题；General Training Task 1 信件暂不在此工作流范围内。

客户端配置见 [MCP 配置说明](skills/ielts-buddy/references/setup.md)。

## 安全与数据使用

- 只读取用户主动提供或明确放入任务范围的作文、DOCX、阅读材料、听力文本、答案和学习偏好。
- 可能在本地创建 DOCX 报告。
- 可能在 `~/.ielts-buddy` 下维护本地 SQLite 学习镜像和离线队列。
- 用户授权 MCP 后，可能把学习事件、词汇复习结果或练习请求发送到 IELTS Buddy 服务。
- 不包含 IELTS Buddy 应用源码、私有用户数据、题库数据、课程内容、第三方练习素材、完整官方评分标准文本或模型密钥。

## 仓库边界

这个仓库只保存可公开分发的 Skill 指令、脚本、引用资料和验证工具。

写作批改工作流改编自 Aaron Liang 的 MIT 许可 IELTS writing review Skills，许可文件见 [ielts-writing-review-skills.txt](skills/ielts-buddy/licenses/ielts-writing-review-skills.txt)。新的学习会话工作流参考了 MIT 许可的语言学习和文档类 Skills，来源说明见 [third-party-skill-sources.txt](skills/ielts-buddy/licenses/third-party-skill-sources.txt)。

IELTS Buddy 服务返回的材料和数据仍遵守其对应权利和条款。

## 验证

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
```

## 关键词

雅思 AI、雅思 Agent、雅思 Skill、IELTS Skills、IELTS Buddy、雅思作文批改、IELTS Writing Task 1、IELTS Writing Task 2、雅思小作文批改、雅思大作文批改、DOCX 批注、Word 批改、雅思单词卡、雅思词汇、雅思阅读复盘、雅思听力精听、雅思口语练习、MCP、Codex Skills、Claude Code Skills、Cursor、SkillHub、英语学习资源推荐。

## License

本仓库的 Skill 指令和工具代码使用 [MIT License](LICENSE) 发布。
