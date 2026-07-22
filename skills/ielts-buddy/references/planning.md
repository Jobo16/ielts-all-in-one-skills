# Learner Context And Planning

## Learner Context

Use `ielts_learner_read_profile` to read skill profiles, footprints, recent activity, and practice-derived weak points. Treat missing data as unknown rather than as a low score.

## Exam Preparation Plans

Use `ielts_exam_prep_inspect` to read planning context before creating a plan. The local Agent writes the plan.

Inspect first. Ask only for planning fields still missing after inspection.

Do not call a server workflow whose job is to generate or refresh the plan text. If a data-only persistence capability exists, use it after the local plan is written and shown. Otherwise return the local plan or generate a DOCX route workbook through `../workflows/daily-study-loop/WORKFLOW.md`.

## Study Plans

Persistent learning plan records use the server-side `ielts_study_plans_*` data capabilities. Web and local Agents operate the same records, and the website's Scheduled view is a read-only projection of those records. The local Agent owns plan drafting, review, tradeoff decisions, and task selection.

- Read with `ielts_study_plans_list`, `ielts_study_plans_get`, and `ielts_study_plans_next_actions`.
- Create by drafting locally from learner context, showing the draft, and calling `ielts_study_plans_create` only after explicit confirmation.
- Before changing, rescheduling, or deleting a plan, read the current revision and show a concise change summary. Write only after explicit confirmation.
- A user statement that they completed a task is sufficient intent to call `ielts_study_plans_update_task`; read the plan again to verify the persisted status.
- Store completed learning activity as learning events. Never store a plan as a `plan.updated` event.
- Do not call `ielts_study_plans_draft` or `ielts_study_plans_review` if the manifest describes server-side generation, review, or AI acceptance checks. Run the local workflow below instead.

Thread-local working steps may guide the current conversation, but they are not persistent study plans. Do not create a separate local plan or scheduled AI workflow.

## Local Plan Draft Workflow

1. Read learner profile, recent footprints, learning events, route progress, vocabulary state, and explicit user constraints.
2. Identify the primary constraint: deadline, weak skill, missing route foundation, vocabulary gap, or consistency.
3. Build a small plan:
   - 1 clear goal;
   - 3-7 tasks;
   - one success criterion per task;
   - one review checkpoint;
   - browser URLs only for browser-owned activities.
4. Explain the tradeoff in Chinese: why this plan chooses this first action and what it intentionally postpones.
5. Ask for confirmation before persistence.
6. Persist the approved local plan with `ielts_study_plans_create` or `ielts_study_plans_update`.

## Local Plan Review Workflow

Use this when the learner asks “这个计划合理吗 / 帮我检查计划 / 调整学习计划”.

1. Read the current plan and latest learner evidence.
2. Check:
   - task count fits available time;
   - the first task is actionable today;
   - route tasks, vocabulary, practice, and review are balanced;
   - weak-area work is backed by evidence;
   - browser-owned tasks include links or required returned artifacts;
   - every task has a completion signal.
3. Return one of:
   - `可执行`: no structural issue;
   - `需要小改`: 1-2 changes;
   - `需要重排`: order or scope is wrong;
   - `信息不足`: missing deadline, target band, current level, or time budget.
4. If changes are needed, produce a patch-style summary:

```text
计划检查：需要小改
保留：<what remains>
调整：<change>
原因：<evidence>
今天先做：<one task>
```

5. Only call `ielts_study_plans_update` after the user confirms the local review result.
