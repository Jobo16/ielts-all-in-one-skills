# Practice

Use these tools for IELTS Buddy question-bank and practice sessions:

- `ielts_practice_search_parts`: search listening, reading, speaking, or writing parts.
- `ielts_practice_start_session`: create a practice session from a part or source topic.
- `ielts_practice_read_session`: read an owned practice or mock session.
- `ielts_practice_submit_session`: submit answers and persist grading results.
- `ielts_practice_recent_activity`: read recent practice activity.

## Find And Start

1. Ask for the subject or infer it only when the user's request is explicit.
2. Search before starting a session unless the user already supplied a valid part ID or source topic ID.
3. Present a compact choice when several parts match.
4. Start the selected part and return the session ID and next action.

## Read And Submit

1. Read the session before modifying it.
2. Preserve each answer's `slotKey`; do not infer missing slot keys.
3. Confirm the user intends to submit when submission will finalize or grade the attempt.
4. Submit only the answers provided by the user.
5. Verify the returned session status, score, and grading result before reporting completion.

Use recent activity and learner profile data to identify patterns, but do not claim a weakness from one isolated answer.
