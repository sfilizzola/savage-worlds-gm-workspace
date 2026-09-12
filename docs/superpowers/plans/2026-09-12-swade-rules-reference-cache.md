# SWADE Rules Reference Cache Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Wire the lazy, agent-only SWADE rules reference cache into the workspace's rules-authority workflow, so future tasks check `sources/systems/SWADE/reference/` before opening the 212-page core PDF.

**Architecture:** Pure documentation change — no application code. Four independent markdown edits: two existing policy files (`GM.md`, `rules/RULES.md`) gain new steps/clarifiers, one existing catalog file (`sources/systems/SWADE/README.md`) gains a pointer, and one new convention file (`sources/systems/SWADE/reference/README.md`) is created. No topic reference files (e.g. `character-creation.md`) are created by this plan — those are built lazily by later, unrelated tasks per the new workflow.

**Tech Stack:** Markdown only.

**Spec:** `docs/superpowers/specs/2026-09-12-swade-rules-reference-cache-design.md`

## Global Constraints

- Reference files under `sources/systems/SWADE/reference/` are agent-only: never printed, never surfaced in `RUN.md` or any player-facing handout.
- Reference files are a non-authoritative lookup cache — they do not add a new rung to `rules/RULES.md`'s precedence list; the SWADE PDF remains sole authority.
- No topic files (`character-creation.md`, `combat.md`, etc.) are created in this plan — the directory starts with only its own `README.md`.
- Scope for this plan is SWADE core only; Weird War II / Deadlands Noir are untouched.
- Every edit must be exact — verification steps grep for the literal inserted text, not an approximation.

---

### Task 1: Insert the reference-cache check into `GM.md`'s Rules authority steps

**Files:**
- Modify: `GM.md` (the numbered list under `## Rules authority`, currently lines 24-29)

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: nothing consumed by other tasks — this is a standalone policy edit. (The convention it references, `sources/systems/SWADE/reference/`, is created in Task 4; order between Task 1 and Task 4 does not matter since this is prose, not executable code.)

- [ ] **Step 1: Replace the 6-step list with the 8-step version**

Find this exact block in `GM.md`:

```markdown
1. Read the adventure's active configuration.
2. Check whether an explicit active house rule applies.
3. Otherwise consult the SWADE Fifth Printing (2023) core PDF.
4. Consult only the setting modules declared active for the adventure.
5. If an older setting rule conflicts with SWADE, use SWADE unless an explicit house rule says otherwise.
6. Record the source title and page or section beside prepared mechanics when practical.
```

Replace it with:

```markdown
1. Read the adventure's active configuration.
2. Check whether an explicit active house rule applies.
3. Check `sources/systems/SWADE/reference/` for a topic file covering the need. If one exists and covers the case, use it directly instead of the PDF.
4. If no reference file exists, or it doesn't cover the specific case, consult the SWADE Fifth Printing (2023) core PDF directly for that gap.
5. After consulting the PDF, create the reference file if none existed, or extend the existing one with the newly-covered material, so the next task doesn't re-pay that cost.
6. Consult only the setting modules declared active for the adventure.
7. If an older setting rule conflicts with SWADE, use SWADE unless an explicit house rule says otherwise.
8. Record the source title and page or section beside prepared mechanics when practical.
```

- [ ] **Step 2: Verify the edit landed exactly**

Run: `grep -n "Check \`sources/systems/SWADE/reference/\` for a topic file" GM.md`
Expected: one match, and `grep -c "^[0-9]\. " GM.md` restricted to this section shows 8 numbered lines (spot-check by reading the section back — the list must read 1 through 8 with no gaps or repeats).

- [ ] **Step 3: Commit**

```bash
git add GM.md
git commit -m "Add reference-cache check to GM.md rules authority steps"
```

---

### Task 2: Add the non-authority clarifier to `rules/RULES.md`

**Files:**
- Modify: `rules/RULES.md` (the `## Operational precedence` section)

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: nothing consumed by other tasks.

- [ ] **Step 1: Insert a clarifying paragraph after the precedence list**

Find this exact block in `rules/RULES.md`:

```markdown
1. **Explicit active house rule:** a deliberate override, limited to its written scope and declared by the adventure.
2. **SWADE Fifth Printing (2023):** default and permanent authority for all mechanics.
3. **Active setting module:** may add compatible setting rules and content; it does not silently replace SWADE.
4. **Recorded ruling:** a dated interpretation for an unclear table case, not a general override.
5. **Co-GM suggestion:** non-authoritative until verified or approved.

An inactive source has no mechanical effect.
```

Replace it with:

```markdown
1. **Explicit active house rule:** a deliberate override, limited to its written scope and declared by the adventure.
2. **SWADE Fifth Printing (2023):** default and permanent authority for all mechanics.
3. **Active setting module:** may add compatible setting rules and content; it does not silently replace SWADE.
4. **Recorded ruling:** a dated interpretation for an unclear table case, not a general override.
5. **Co-GM suggestion:** non-authoritative until verified or approved.

An inactive source has no mechanical effect.

`sources/systems/SWADE/reference/` is a non-authoritative lookup cache of item 2 — it is not a new rung in this list. If a reference file is ever found to disagree with the PDF, the PDF wins; correct the file in place immediately.
```

- [ ] **Step 2: Verify the edit landed exactly**

Run: `grep -n "non-authoritative lookup cache of item 2" rules/RULES.md`
Expected: one match.

- [ ] **Step 3: Commit**

```bash
git add rules/RULES.md
git commit -m "Clarify SWADE reference cache is non-authoritative in RULES.md"
```

---

### Task 3: Point `sources/systems/SWADE/README.md` at the new reference directory

**Files:**
- Modify: `sources/systems/SWADE/README.md`

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: nothing consumed by other tasks.

- [ ] **Step 1: Append a paragraph about the reference directory**

Find this exact block in `sources/systems/SWADE/README.md`:

```markdown
Consult this PDF before creating or changing mechanics. Quick references and setting modules remain subordinate unless an explicit active house rule states a scoped override.
```

Replace it with:

```markdown
Consult this PDF before creating or changing mechanics. Quick references and setting modules remain subordinate unless an explicit active house rule states a scoped override.

`reference/` holds lazily-built, agent-only markdown files distilling specific topics from this PDF (see `reference/README.md` for the convention). If this PDF is ever replaced with a different printing, re-verify every `reference/*.md` file whose `source_sha256` frontmatter matches the SHA-256 above before trusting it again.
```

- [ ] **Step 2: Verify the edit landed exactly**

Run: `grep -n "re-verify every \`reference/\*.md\`" sources/systems/SWADE/README.md`
Expected: one match.

- [ ] **Step 3: Commit**

```bash
git add sources/systems/SWADE/README.md
git commit -m "Point SWADE README at the new reference/ cache directory"
```

---

### Task 4: Create `sources/systems/SWADE/reference/README.md`

**Files:**
- Create: `sources/systems/SWADE/reference/README.md`

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: the convention document that Tasks 1-3's cross-references point to (order-independent, since all four are prose edits with no build/import step).

- [ ] **Step 1: Create the directory and file with the exact content below**

Create `sources/systems/SWADE/reference/README.md`:

```markdown
# SWADE reference cache

Agent-only, lazily-built markdown files distilling specific SWADE topics
(character creation, combat, edges/hindrances, etc.) from the core PDF at
`../SWADE_Savage_Worlds_Adventure_Edition_Fifth_Printing_2023.pdf`. These
files are never printed and never shown to players — see `GM.md`'s "Rules
authority" section for when to check, create, and extend them.

## Convention

- **One file per topic**, flat in this directory, named as a slug
  (`character-creation.md`, `combat.md`, ...). Topics don't have to match
  the book's chapter boundaries — group whatever content actually gets
  looked up together.
- **Check before creating.** Before adding a new topic file, check whether
  an existing file already covers the topic (even under a different
  name), and extend it instead of creating a near-duplicate.
- **Frontmatter contract** on every file:

  ```yaml
  ---
  topic: <slug>
  source: SWADE Fifth Printing (2023)
  source_sha256: <must match ../README.md>
  pages_consulted: <page ranges actually read>
  built: <YYYY-MM-DD>
  ---
  ```

- **Content** may be verbatim excerpts, recreated tables, or paraphrase —
  whichever is most accurate. Cite the page for each claim.
- **Non-authoritative.** These files are a lookup cache of the SWADE PDF,
  not a new rung in `rules/RULES.md`'s precedence. If a file is ever found
  to disagree with the PDF, the PDF wins — correct the file in place
  immediately, no versioning needed.
- **Not every lookup needs a file.** Only create/extend one for a topic
  that plausibly recurs.
```

- [ ] **Step 2: Verify the file exists with the right content**

Run: `test -f sources/systems/SWADE/reference/README.md && grep -c "^" sources/systems/SWADE/reference/README.md`
Expected: file exists; line count matches the content written (non-zero, no truncation).

- [ ] **Step 3: Commit**

```bash
git add sources/systems/SWADE/reference/README.md
git commit -m "Add SWADE reference cache convention doc"
```

---

## Final check (after all four tasks)

- [ ] **Step 1: Confirm no topic files were created**

Run: `find sources/systems/SWADE/reference -type f`
Expected: exactly one file, `sources/systems/SWADE/reference/README.md`.

- [ ] **Step 2: Confirm all four commits are present**

Run: `git log --oneline -4`
Expected: four commits matching Tasks 1-4's messages, newest first.
