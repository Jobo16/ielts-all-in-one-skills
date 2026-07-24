# My Vocabulary Book

IELTS Buddy provides one cloud-backed personal vocabulary book shared by the web Agent, local Agents, and learning modules.

## Tools

- `ielts_vocabulary_list`: search or list saved words and their sources.
- `ielts_vocabulary_progress`: read learning-state counts and per-word progress for built-in wordbooks or My Vocabulary Book.
- `ielts_vocabulary_prepare_cards`: prepare data-only local flashcards from a selected built-in or personal wordbook while avoiding recently reviewed words when possible.
- `ielts_vocabulary_add`: add or enrich words and record where they came from.
- `ielts_vocabulary_update`: correct an entry or update `learningState` to `new`, `learning`, `review`, `relearning`, or `mastered`.
- `ielts_vocabulary_record_review`: record a local flashcard review result with rating `again`, `hard`, or `good`.
- `ielts_vocabulary_delete`: remove one entry after confirmation.

When the user asks to remember, collect, or review a word or phrase, save it with `ielts_vocabulary_add`. Use `sourceType=agent` for direct conversation additions; use a more specific source such as `practice`, `course`, or `reading_lexicon` when known. Include `sourceId`, `sourceTitle`, and the source sentence when available.

Words are deduplicated case-insensitively. Adding an existing phrase enriches its metadata and records another source instead of creating a duplicate.

For local flashcard practice, call `ielts_vocabulary_prepare_cards` and return the card data in the conversation. Do not provide a browser link unless the user explicitly asks to open the web app.

For an interactive local session, use the installed `$ielts-vocabulary-coach` Skill: one card at a time, active recall before reveal, concise feedback, and `ielts_vocabulary_record_review` after each answered card.

Common local-card inputs:

- “给我 10 个核心词，不要和上次重复”：`source=builtin`, `setId=core`, `limit=10`, `mode=mixed`, `excludeRecentlyReviewedDays=7`.
- “听力词书新词”：`source=builtin`, `setId=listening`, `mode=new`.
- “阅读词书复习到期词”：`source=builtin`, `setId=reading`, `mode=due`.
- “复习我的错词/弱词”：use `mode=weak`; choose `source=builtin` for built-in wordbooks or `source=personal` for My Vocabulary Book.

After each answered card, call `ielts_vocabulary_record_review` with the same `source`; for built-in words pass `setId` and `entryId`, and for personal words pass `id`. Do not pick a fresh random batch from `ielts_vocabulary_list` alone, because that ignores history and can repeat the same words.

The built-in core, listening, and reading word books are read-only study content. “My Vocabulary Book” is the user's writable collection and is the destination for words produced by all other modules and Agents.
