# Learner Context And Planning

## Learner Context

Use `ielts_learner_read_profile` to read skill profiles, footprints, recent activity, and practice-derived weak points. Treat missing data as unknown rather than as a low score.

## Exam Preparation Plans

- `ielts_exam_prep_inspect`: read planning context before creating a plan.
- `ielts_exam_prep_start_plan`: generate and persist an exam-prep plan artifact.
- `ielts_exam_prep_refresh_plan`: refresh an existing plan artifact from current context.

Inspect first. Ask only for planning fields still missing after inspection.

## Study Plans

All persistent learning plans use the server-side `ielts_study_plans_*` capabilities. Web and local Agents operate the same records, and the website's Scheduled view is a read-only projection of those records.

- Read with `ielts_study_plans_list`, `ielts_study_plans_get`, and `ielts_study_plans_next_actions`.
- Create by calling `ielts_study_plans_draft`, showing the draft, and calling `ielts_study_plans_create` only after explicit confirmation.
- Before changing, rescheduling, or deleting a plan, read the current revision and show a concise change summary. Write only after explicit confirmation.
- A user statement that they completed a task is sufficient intent to call `ielts_study_plans_update_task`; read the plan again to verify the persisted status.
- Store completed learning activity as learning events. Never store a plan as a `plan.updated` event.

Thread-local working steps may guide the current conversation, but they are not persistent study plans. Do not create a separate local plan or scheduled AI workflow.
