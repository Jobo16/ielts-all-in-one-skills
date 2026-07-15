# Example Gallery

Use this gallery to show new users what IELTS Buddy can produce. Keep examples short and actionable.
Use Simplified Chinese prompts and descriptions by default.

| 场景 | 用户可以这样问 | Agent 输出 |
| --- | --- | --- |
| 首次使用 | `使用 $ielts-buddy 介绍这个 Skill 能做什么。` | 入门提示、可用模式、一个推荐的第一步学习动作。 |
| Task 2 作文批改 | `帮我批改这篇 Task 2，并输出 Word 文档。` | 带真实 Word 批注、斜体改写、分数参考、中文重点反馈和 model essay 的 DOCX。 |
| Task 1 小作文批改 | `结合图表帮我批改 Task 1，并输出 DOCX。` | 带图表理解、中文批注、分数参考、数据表达改写和四段 model answer 的 DOCX。 |
| 写作二改 | `检查我二改后的作文有没有解决上次批注。` | 二改报告 DOCX，包含已修/未修问题、分数变化参考、剩余问题和下一轮改写目标。 |
| 单词卡 | `今天给我 10 个词书单词，不要重复学过的。` | 主动回忆单词卡、例句、中文反馈、复习进度更新，可选周复习表。 |
| 阅读复盘 | `把我的阅读错题整理成证据图。` | 阅读证据图 DOCX，包含答案证据、同义替换、陷阱解释、错误类型和微训练。 |
| 听力复盘 | `根据这段精听文本和错题做一个听力错题本。` | 听力错题本，包含重听重点、原文片段、错误原因、词汇和训练。 |
| 口语教练 | `复盘这些口语回答，给我更自然的表达。` | 口语反馈 DOCX，包含分数参考、自然改写、可复用表达和下一题。 |
| 雅思路线 | `根据我的雅思路线进度安排今天学习。` | 本地学习计划或课程路线学习手册，包含下一步行动、达标标准和网页链接。 |
| 学习资源推荐 | `推荐适合 B1-B2 的雅思听力资源，并做一周计划。` | 来自内置资源库的排序推荐、使用方法、回传任务，可选推荐 DOCX。 |

## Demo Prompts For Visible Outputs

Use these when the user wants to see the effect:

```text
使用 $ielts-buddy 根据我粘贴的一篇短 Task 2 作文生成批改 DOCX。
```

```text
使用 $ielts-buddy 把我的阅读答案整理成证据图 DOCX。
```

```text
使用 $ielts-buddy 根据今天的单词卡结果生成词汇周复习表。
```

```text
使用 $ielts-buddy 根据这段听力文本和错题生成听力错题本。
```

```text
使用 $ielts-buddy 推荐 5 个听力资源，并生成一周学习包。
```

## How To Explain The Value

- Chat answers are good for quick coaching and next actions.
- DOCX outputs are better when the learner needs comments, tables, rewrites, score movement, or a printable study artifact.
- Browser links are best when the task requires playback, timed practice, mock tests, or copyrighted course/question-bank material.
- The local Agent owns learning policy; the service supplies data, state, media, and browser surfaces.
