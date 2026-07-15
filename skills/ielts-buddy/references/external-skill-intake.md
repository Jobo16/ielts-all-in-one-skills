# External Skill Intake

IELTS Buddy should grow from Skills first. Hosted services provide data, media, auth, durable state, and browser-only execution surfaces. Local Skills own the teaching rules, task sequencing, feedback style, review policy, and visible deliverables.

## Intake Rule

1. Prefer copying and adapting complete MIT or Apache-licensed Skills when the source has a clear workflow and can be narrowed to IELTS.
2. Do not copy proprietary Skills into this public repository. Use only generic engineering facts that are independently implementable.
3. Do not mix ShareAlike content into this MIT repository. If a ShareAlike source is worth using, keep it as a separate optional package or rewrite the method from first principles.
4. When substantially adapting an MIT source, keep the source URL and license notice in `licenses/`.
5. After import, remove generic app behavior and make the Skill obey the IELTS Buddy boundary: server data in, local learning workflow out.

## Current Source Decisions

| Source | License | Use |
| --- | --- | --- |
| `m98/fluent` | MIT | Copy-adapt the adaptive session, vocabulary drill, spaced review, feedback formatter, session analyzer, writing, and typed speaking patterns. |
| `tianmind-studio/english-coach` | MIT | Copy-adapt the “answer first, then concise corrections” pattern and recurring-error detection. |
| `hamsamilton/lang-tutor` | MIT | Copy-adapt persistent tutor mode, language-setting resolution, and feedback-mode separation. |
| `claude-office-skills/skills` | MIT | Copy-adapt lightweight `python-docx` document creation patterns when enough for a workflow. |
| `appautomaton/document-skills` | MIT | Copy-adapt OOXML editing/redlining/validation patterns when a workflow needs anchored comments or tracked edits. |
| `anthropics/skills/docx` | Proprietary | Do not copy. The public repo already has original DOCX scripts; keep using original OOXML code and validation. |
| `GarethManning/education-agent-skills` | CC BY-SA 4.0 | Do not copy into MIT. Useful as a checklist for learning-science concepts only. |
| Low-install or unclear-license language tutor Skills | Mixed/unclear | Do not import until the source is verified. |

## Copy-Adapt Checklist

For each imported workflow:

1. Clone to a temporary source folder.
2. Read the source `SKILL.md`, bundled references, scripts, and license.
3. Extract the core learning move, not the original branding or UI.
4. Replace generic data stores with IELTS Buddy tools or `learning_store.py`.
5. Define whether the workflow is:
   - local-only;
   - data-plus-link;
   - browser-first with local follow-up;
   - visible-document output.
6. Add an IELTS-specific quality bar and validation step.
7. Add source attribution if any substantial text, structure, or script is adapted.

## Local/Server Boundary

Keep these in Skills:

- choosing the next activity;
- active recall, hinting, feedback timing, and retry rules;
- IELTS scoring interpretation and error taxonomy;
- vocabulary drill modes and spaced review policy;
- teacher-style writing correction structure;
- report/document layout decisions;
- short-term local mirrors and offline queues.

Keep these in IELTS Buddy service:

- authenticated user state and cross-device progress;
- built-in wordbooks and per-word progress;
- question-bank materials and copyrighted practice content;
- course route and route progress;
- audio playback, timed practice, mock tests, and browser-owned sessions;
- durable event log and OAuth.

The service may return recommendations as data, but the portable Skill must still be able to explain and execute the local learning policy without delegating the teaching decision to the server.

