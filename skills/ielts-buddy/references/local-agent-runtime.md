# 本地 Agent Runtime 边界

IELTS Buddy 服务端提供数据、媒体、权限、跨设备状态和网页执行面。本地 Skill 负责教学判断、开放题批改、计划推理、材料匹配、反馈生成和可见文档输出。

## 调用 MCP 前先判定

如果 MCP 工具只是读取或保存 caller-provided 数据，可以使用。如果工具描述会让服务端执行以下动作，不要从本地 Skill 调用：

- AI / teacher-style review / fresh review / feedback；
- generate / draft / review 学习计划；
- match suitable questions / 自动匹配题目；
- writing 或 speaking 的开放题评分；
- 任何把教学判断交给 server agent-runtime 的动作。

遇到这类工具时，改走下面的本地流程。服务端只接收最终数据、学习事件、进度、文件链接或浏览器链接。

## 替代映射

| 原本可能放在云端 agent-runtime 的任务 | 本地 Skill 执行 | 允许的 MCP/服务端动作 |
| --- | --- | --- |
| Writing Task 1 首轮批改 | 直接使用现有 `../workflows/ielts-task1-review/WORKFLOW.md`；不要在本文件复制批改步骤 | 读取题目/历史；保存用户提交的原文、本地评分摘要、DOCX 元数据或学习事件 |
| Writing Task 2 首轮批改 | 直接使用现有 `../workflows/ielts-task2-review/WORKFLOW.md`；不要在本文件复制批改步骤 | 同上 |
| Writing 二改 | 直接使用现有 `../workflows/writing-revision-loop/WORKFLOW.md`；不要另写二改流程 | 保存 revision 文本、本地 revision report 摘要或学习事件 |
| Reading/Listening 客观题判分 | 客观题可用答案 key 或已提交结果；本地负责错因、同义替换、听力错因和微训练 | 读取/提交客观题 session、读取结果、记录学习事件 |
| Writing/Speaking 开放题判分 | 本地写作/口语 workflow 给分数参考和反馈 | 只保存 caller-provided 结果；不能让服务端生成反馈 |
| Study plan draft/review | `planning.md`：本地读取画像、路线、进度后起草、审查、改计划 | 创建/更新本地 Agent 已写好的计划记录和任务状态 |
| Speaking topic weaving | `../workflows/speaking-topic-builder/WORKFLOW.md`：本地从 learner story、目标 part、题库数据中选择 exact questions 并写素材 | 保存本地已选 question links、story、chunks、练习顺序；不能让服务端自动匹配 |
| Reading lexicon | `../workflows/ielts-reading-lexicon/WORKFLOW.md`：本地抽词、批注、例句、复习提示并生成 DOCX | 可选保存词条和复习进度 |
| Resource recommendation | `../workflows/learning-resource-recommender/WORKFLOW.md`：本地从内置目录筛选并给使用方法 | 不需要云端 AI |

## 本地执行要求

1. 先读数据，再做教学判断。读取范围限于用户授权的 IELTS Buddy 数据、用户提供文件和 Skill 内置资源。
2. 明确把“证据”和“建议”分开：题目、答案、历史记录是证据；批改、计划、推荐和复盘是本地 Agent 的推理结果。
3. 开放题给分必须叫“分数参考”，并说明不等同于官方成绩。
4. 需要写回服务端时，只写本地 Agent 已经完成的结果，不写“请服务端帮我生成/批改/匹配”的请求。
5. 如果当前 manifest 只有云端 AI 版本的工具，跳过该写回，直接交付本地结果，并说明需要 data-only 接口才能同步。
