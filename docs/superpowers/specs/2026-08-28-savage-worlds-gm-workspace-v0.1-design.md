# Savage Worlds GM Workspace v0.1 - Approved Design

## Purpose

Create a reusable English-first authoring repository for Savage Worlds one-shots, arcs, and campaigns. The workspace helps a co-GM expand the GM's ideas while preserving agency, rules accuracy, maintainable canon, and table usability.

## Decisions carried forward

- SWADE Fifth Printing (2023) is the permanent core rules authority.
- Weird War II is installed but optional and must be activated per adventure.
- House rules are explicit, scoped overrides only.
- Both pregenerated and player-supplied character workflows are supported.
- Every adventure declares Rank, player count, active modules, supernatural level, historical-accuracy requirements and sources, house rules, language, format, and runtime.
- Stories use predetermined truths and objectives with flexible situations rather than a fixed scene chain.
- Failure changes circumstances but does not automatically halt progress toward the main plot.
- Preparation must challenge single points of failure.
- Early-session PC removal is mitigated; later lethal consequences remain possible.
- `RUN.md` is a compiled, table-facing document with verified mechanics at the point of use.
- Source material, canon, prep, and session records remain distinct.

## Architecture

The repository has six operational layers: instructions, sources, rules, world canon, adventures, and templates. Source PDFs are read-only dependencies. Modular adventure files are human-maintained source files. `RUN.md` intentionally duplicates the information needed during play and is rebuilt whenever its sources change.

## Verification

Each adventure uses configuration, design, mechanics, historical, lethality, and compilation checklists. Mechanical claims must point to an authoritative title and page or section. Unsupported mechanics are flagged for a GM decision rather than invented.

## Scope

v0.1 provides the framework and templates, not a sample adventure, extracted rule compendium, automated compiler, or digital character builder. Those should be added only after the framework is tested with a real adventure.

