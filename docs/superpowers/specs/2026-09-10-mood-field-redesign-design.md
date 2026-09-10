# Story-Point Mood Field - Approved Design

## Purpose

The Mood field established in the original Adventure RUN Skeleton design (`2026-08-31-adventure-run-skeleton-design.md`) splits scene-setting into four labeled one-line bullets: Climate, See, Hear, Feel. In practice (see `operation-hinterland/RUN.md`) this reads as a list of disconnected sensory tags rather than something a GM can naturally paraphrase to the table. Published one-shot modules (D&D Adventurers League, Pathfinder) instead present the equivalent read-aloud/scene-setting content as a single flowing paragraph, with GM-only information kept separate rather than tagged inline. This design replaces the four-bullet Mood format with that single-paragraph form.

## Decision

Replace the four labeled sub-bullets under **Mood (table):** with one flowing paragraph (~40-80 words, present tense) that weaves climate/weather, what's seen, and what's heard into a description of the place, ending on the scene's tension or tone as its natural last clause. All existing hard constraints carry over unchanged: player-perceivable only, not a verbatim read-aloud, no secrets, unearned names, historical footnotes, or GM editorials.

An optional trailing "Tone:" line was considered (for situations where urgency isn't obvious from description alone) and explicitly rejected in favor of the pure single-paragraph form — tone should be conveyed by how the paragraph is written, not by a separate tag.

## Architecture

- `templates/adventure/SKELETON.md` — Situation block template's Mood field becomes a single paragraph slot; the Climate/See/Hear/Feel sub-bullets are removed (main and nested-location blocks). The Notation table's Mood row, the "When a field is required" table row, and the compile gate checklist item are rewritten to describe the paragraph form instead of the four-part list.
- `GM.md` line 157 — rewritten to describe the paragraph form instead of the four-part checklist.
- `templates/adventure/QUALITY.md` item 9 — the parenthetical `(Climate / See / Hear / Feel)` is replaced with "a single player-perceivable paragraph describing the place."
- `templates/adventure/RUN.md` (the copy-me RUN template, distinct from the `SKELETON.md` contract) — same paragraph-form rewrite at its Mood reference and nested-location sensory-frame line, so newly started adventures aren't seeded with the old format.
- `templates/location.md` and `templates/adventure/locations.md` — the **First impression** field, which `SKELETON.md` states Mood is compiled from, is rewritten to the same single-paragraph form. Left as four labeled lines, First impression would keep seeding Mood in the old shape regardless of the RUN-side fix.
- No change to any other situation-block field (Spoken lines, Discoverable, GM Note, Pressure/escalation, Failure changes, Reachable next points, Optional/PC hook, at-hand boards) or to document-level order.

## Worked example

Before (current format, Story Point 0b, `operation-hinterland/RUN.md`):

> **Mood (table):** Paraphrase. Not a read-aloud. No secrets.
>
> - **Climate:** Colder and darker than the classroom. Cloud. Wind through the airframe.
> - **See:** Four in one stick. No readable fields. Flak flashes somewhere under the flight — not a town they can name.
> - **Hear:** Engines. Wind. Bursts. Then a crew voice and a green light.
> - **Feel:** Thrill. Not a fight. The drop is already worse than the briefing.

After (new format):

> **Mood (table):** Colder and darker than the classroom, wind cutting through the airframe as engines drone and bursts flash somewhere below. Four in one stick, no readable fields, no town they can name — just flak flashes under the flight path, not a fight. It's already worse than the briefing.

## Out of scope

- Rebuilding `operation-hinterland/RUN.md` (or any other existing compiled `RUN.md`) to the new Mood format. Flagged for a later rebuild pass, not required by this change.
- Rewriting already-drafted "First impression" content in existing campaigns/adventures (e.g. `campaigns/no-further-action/world/locations/*.md`, `campaigns/no-further-action/vozes-sem-corpo/locations.md`, `operation-hinterland`) that still uses the four-line format. Only the copy-me templates are updated; existing written content is untouched, same as existing compiled `RUN.md` files.
- Changing any other situation-block field or document-level order.
- Changing the 120-point quality scoring weights — only the wording of item 9's guidance changes, not its point value.
- Reintroducing a labeled tone/feel sub-field.
