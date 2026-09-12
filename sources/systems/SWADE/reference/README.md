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
