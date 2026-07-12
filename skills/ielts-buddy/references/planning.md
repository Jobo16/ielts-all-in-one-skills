# Learner Context And Planning

## Learner Context

Use `ielts_learner_read_profile` to read skill profiles, footprints, recent activity, and practice-derived weak points. Treat missing data as unknown rather than as a low score.

## Exam Preparation Plans

- `ielts_exam_prep_inspect`: read planning context before creating a plan.
- `ielts_exam_prep_start_plan`: generate and persist an exam-prep plan artifact.
- `ielts_exam_prep_refresh_plan`: refresh an existing plan artifact from current context.

Inspect first. Ask only for planning fields still missing after inspection.

For an Agent-owned working plan, store the complete current plan as a `plan.updated` learning event with `objectType=plan` and a stable `objectId`. Local Agents write it through `learning_store.py`; web-only Agents push the same event through `ielts_learning_push_events`. Append another event for each revision instead of overwriting history.

## Scheduled Tasks

Scheduled-task and structured-plan operations evolve independently from the Skill release. Inspect the live capability manifest and the connected MCP tool list before choosing an operation. Use the current `ielts_scheduled_tasks_*` or `ielts_study_plans_*` tool exposed by the server instead of assuming a tool exists from its name here.

Keep recurring AI workflows separate from Agent-owned learning plans. Use server-side structured plans only when the user explicitly wants a shared website plan. State the trigger time and timezone clearly before creating or changing a schedule. Confirm deletion and verify every persisted result.
