# My Vocabulary Book

IELTS Buddy provides one cloud-backed personal vocabulary book shared by the web Agent, local Agents, and learning modules.

## Tools

- `ielts_vocabulary_list`: search or list saved words and their sources.
- `ielts_vocabulary_add`: add or enrich words and record where they came from.
- `ielts_vocabulary_update`: correct an entry or update `masteryLevel` to `new`, `learning`, or `known`.
- `ielts_vocabulary_delete`: remove one entry after confirmation.

When the user asks to remember, collect, or review a word or phrase, save it with `ielts_vocabulary_add`. Use `sourceType=agent` for direct conversation additions; use a more specific source such as `practice`, `course`, or `reading_lexicon` when known. Include `sourceId`, `sourceTitle`, and the source sentence when available.

Words are deduplicated case-insensitively. Adding an existing phrase enriches its metadata and records another source instead of creating a duplicate.

The built-in core, listening, and reading word books are read-only study content. “My Vocabulary Book” is the user's writable collection and is the destination for words produced by all other modules and Agents.
