# SWADE rules reference cache — design

Date: 2026-09-12

## Problem

`sources/systems/SWADE/` holds the single 212-page SWADE Fifth Printing
(2023) core rulebook as a PDF — the permanent mechanical authority for
every adventure in this workspace (`rules/RULES.md`). Recurring tasks
(character creation, combat, edges/hindrances, gear, etc.) require
re-reading and re-parsing the same pages of that PDF every time they
come up, in every session, because nothing in the repo captures what
was already found. This costs both **navigation** (finding the right
page/section) and **re-derivation** (re-parsing tables, step lists,
and costs from raw PDF text) effort, repeatedly, for the same
material.

## Goal

Build a lazily-populated, per-topic markdown cache of distilled SWADE
content that agents check before opening the PDF, and extend the first
time a gap is found — so the cost of finding and parsing a given topic
is paid once, not once per session.

Scope: **SWADE core rulebook only** for now. Weird War II and Deadlands
Noir remain PDF-only — they're inactive by default and reused far less
than the core book (`rules/RULES.md` edition-compatibility section).
If this proves useful, the same pattern can extend to those sources
later; that is out of scope here.

This cache is **agent-only internal tooling**. It is never printed,
never surfaced in `RUN.md` or any player-facing handout, and is not
subject to `GM.md`'s "short paraphrased reminders only" rule (that rule
governs player/table-facing content). The GM has confirmed the source
material is legally owned and used here in a non-commercial house-rules
context, so reference files may hold direct excerpts, full tables, or
exact wording when that is more accurate than a paraphrase — there is
no forced-paraphrase constraint.

## Non-goals

- Not a new rung in the rules-authority precedence
  (`rules/RULES.md`). The SWADE PDF remains the sole authority for
  rung 2; reference files are a subordinate lookup cache of it.
- Not an upfront, comprehensive rules digest. Nothing is pre-built;
  files are created only when a real task needs a topic that isn't
  covered yet.
- Not extended to Weird War II / Deadlands Noir in this pass.
- Not player-facing or print-tooling related.

## Design

### File structure

```
sources/systems/SWADE/
  SWADE_Savage_Worlds_Adventure_Edition_Fifth_Printing_2023.pdf
  README.md
  reference/
    README.md                  <- convention doc (see below)
    character-creation.md      <- created lazily, one example
    combat.md
    edges-hindrances.md
    ...
```

- Flat directory (no nesting), consistent with `world/npcs/`,
  `world/factions/`, etc.
- Filenames are topic slugs chosen at creation time by whatever task
  first needs them. Topics don't have to mirror the book's chapter
  boundaries — e.g. `character-creation.md` can merge Race, Traits,
  Skills, Edges/Hindrands, and Gear even though SWADE spreads those
  across many pages, because that's how the topic is actually used.
- Before creating a new topic file, check whether an existing file
  already covers the topic (even under a different name) to avoid
  near-duplicate, drifting files.

### Content contract

Each reference file opens with a frontmatter block, then body content
organized for lookup usefulness, not forced to the book's page order:

```markdown
---
topic: character-creation
source: SWADE Fifth Printing (2023)
source_sha256: 373d0066b01b3ce7f889b1de826793f2fe9d978e3a0c168c3febdfe1ead52fbe
pages_consulted: 32-39, 42-58, 61-74
built: 2026-09-12
---

# Character Creation

## Sequence
1. ...

## Race
(table/options, exact costs, p.32-35)

## Traits, Skills, Edges, Hindrances, Gear
...
```

- `source_sha256` must match the hash recorded in
  `sources/systems/SWADE/README.md`, tying the file to the exact PDF
  revision it was built from.
- `pages_consulted` records what was actually read, for traceability
  and spot-checking — not for copyright reasons.
- Body content may be verbatim excerpts, recreated tables, or
  paraphrase — whichever is more accurate for that material.

### Trigger workflow

`GM.md`'s "Rules authority" section (currently a 6-step list) gets a
new step inserted before "consult the SWADE PDF":

1. Read the adventure's active configuration. *(unchanged)*
2. Check whether an explicit active house rule applies. *(unchanged)*
3. **Check `sources/systems/SWADE/reference/` for a topic file
   covering the need.** If one exists and covers the case, use it
   directly — skip the PDF. *(new)*
4. If no reference file exists, or it doesn't cover the specific case
   (an edge case, an unusual combo), consult the SWADE PDF directly
   for that gap. *(renumbered from old step 3)*
5. **After consulting the PDF, create the file if none existed, or
   extend the existing one** with the newly-covered material (same
   frontmatter/citation contract above) — so the next task doesn't
   re-pay that cost. *(new)*
6. Consult only setting modules declared active for the adventure.
   *(renumbered from old step 4)*
7. If an older setting rule conflicts with SWADE, use SWADE unless an
   explicit house rule says otherwise. *(renumbered from old step 5,
   unchanged in content)*
8. Record source + page beside prepared mechanics when practical.
   *(renumbered from old step 6)*

**Extend, don't duplicate.** If a task needs an Edge not yet covered
in an existing `character-creation.md`, the agent adds it to that file
rather than creating an overlapping new file.

**Reference files are a cache, not a rung.** `rules/RULES.md`'s
precedence list is unchanged in structure; it gains a one-line
clarifier under item 2 (SWADE Fifth Printing): reference files are a
non-authoritative lookup cache of it. If a reference file is ever
found to disagree with the PDF, the PDF wins, and the file is
corrected in place immediately — no versioning or history, since these
are tooling artifacts, not session record or canon.

**Not every lookup is worth caching.** A one-off rule that plausibly
never recurs doesn't need a new file. The judgment call ("will this
class of lookup recur") stays with whoever is doing the lookup.

### Concrete file changes

- **`GM.md`** — insert new step 3 in "Rules authority" as above;
  renumber the rest.
- **`rules/RULES.md`** — add one clarifying line under "Operational
  precedence" item 2 (SWADE Fifth Printing) stating reference files
  are a non-authoritative cache of it.
- **`sources/systems/SWADE/README.md`** — add a line noting the
  `reference/` subdirectory and its purpose; note that replacing the
  PDF edition means re-verifying reference files built against the old
  `source_sha256` (this extends the existing "keep the authority
  declaration in RULES.md synchronized" rule from `sources/README.md`
  to also cover reference files).
- **New `sources/systems/SWADE/reference/README.md`** — states the
  convention: frontmatter contract, "extend don't duplicate," flat
  structure, agent-only/never-printed.
- **No topic files created upfront.** The directory starts with only
  its `README.md`; topic files appear lazily as real tasks need them.
- **No changes** to `CLAUDE.md` (already points to `GM.md`/`RULES.md`,
  which carry the new instruction) or to any adventure-level files.

### Maintenance & edge cases

- **Source edition change:** if the SWADE PDF is ever replaced, the
  existing sync rule in `sources/README.md` ("keep the authority
  declaration in RULES.md synchronized") now also means: check each
  `reference/*.md`'s `source_sha256` against the new hash and
  re-verify/rebuild any that changed.
- **Found wrong:** correct the file in place immediately; no
  versioning needed.
- **Not worth caching:** see "not every lookup is worth caching"
  above.

## Testing / validation

There is no executable code in this design — validation is: the next
time a real task needs SWADE content (e.g. character creation), the
agent follows the new `GM.md` step 3, finds no reference file, reads
the PDF, and writes `sources/systems/SWADE/reference/character-creation.md`
per the content contract. A second, later task on the same topic
should then be answerable from that file alone, without opening the
PDF — that's the concrete proof the design works.
