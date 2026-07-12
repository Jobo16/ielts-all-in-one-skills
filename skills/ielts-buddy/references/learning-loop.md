# Local-First Learning Loop

The local Agent and the IELTS Buddy web Agent follow the same loop. The storage adapter differs; the learning policy does not.

## Storage Adapter

When a local filesystem and Python 3 are available, use the bundled zero-dependency store:

```sh
python3 <skill-dir>/scripts/learning_store.py init
python3 <skill-dir>/scripts/learning_store.py snapshot
python3 <skill-dir>/scripts/learning_store.py next
```

The default database is `~/.ielts-buddy/learning.db`. Set `IELTS_BUDDY_HOME` to move it. Do not edit the SQLite database directly.

When no local filesystem is available, use cloud events directly:

- `ielts_learning_pull_events`: read events after a cursor.
- `ielts_learning_push_events`: append events idempotently.

The cloud is a synchronized event copy, not the learning controller.

## Session Loop

1. Read the current snapshot before proposing work.
2. Handle a due review first.
3. Otherwise target the skill with the lowest supported mastery.
4. With no evidence, start a diagnostic listening or reading practice.
5. Ask one task at a time and use hints before answers.
6. Record the outcome immediately after grading.
7. End with one concrete next action; do not produce a dashboard unless asked.

For local objective attempts:

```sh
python3 <skill-dir>/scripts/learning_store.py record-attempt \
  --subject reading \
  --object-type question \
  --object-id <question-id> \
  --skill reading.paraphrase \
  --correct false
```

Use stable IELTS Buddy question, session, plan, or resource IDs as object IDs. For plans and other state changes, use `record-event` with a complete JSON payload:

```sh
python3 <skill-dir>/scripts/learning_store.py record-event \
  --type plan.updated \
  --object-type plan \
  --object-id <plan-id> \
  --payload-json '<complete-plan-json>'
```

## Learning Policy

Mastery uses the five most recent boolean outcomes with increasing recency weights. One observation is capped at `0.50`; two observations are capped at `0.80`. This prevents a lucky answer from becoming mastery while allowing recovery after earlier mistakes.

Review intervals are `1, 3, 7, 14, 30, 60, 90` days after consecutive successful retrievals. An incorrect result is due immediately. The Agent may explain these decisions but must not invent extra precision.

Selection order:

1. Overdue or failed review.
2. Lowest-mastery skill with evidence.
3. Diagnostic practice.

This V1 intentionally uses an explainable model. Do not run BKT, IRT, FSRS parameter optimization, or a separate server-side recommender without sufficient real learner history.

## Cloud Sync

For local-to-cloud sync:

1. Run `outbox --limit 200`.
2. Send the returned `events` unchanged to `ielts_learning_push_events`.
3. After a successful response, run `ack` with every event ID from that batch.
4. Read the local `cloudCursor` from `snapshot`.
5. Call `ielts_learning_pull_events` with that cursor until `hasMore=false`.
6. Save each response to a temporary JSON file or pipe it to `import --input -`.

Never block a learning session because cloud sync is unavailable. Never merge by timestamps or overwrite events; event IDs make append and import idempotent.

## Model Basis

The V1 design adapts three proven open-source patterns:

- DeepTutor: recent evidence with confidence caps and a swappable mastery policy.
- OATutor: prioritize relevant work with the lowest current mastery.
- Learn FASTER and claude-tutor: local learner state, active recall, and spaced review.

The implementation is original and deliberately smaller than those systems.
