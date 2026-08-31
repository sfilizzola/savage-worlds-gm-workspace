# Adventure Quality Coherence Check - Approved Design

## Purpose

Add a prep-only coherence check to the adventure quality gate so a throughline has a beginning that already contains the premise’s problem, essential story points that are causally reachable, and end states that answer the one-sentence premise. After a pass, record a short logic summary of reachable paths. Do not turn this into a scene script or change the 120-point score.

## Decisions

- **Prep only.** Session recaps and canon history are out of scope.
- **Contract is the one-sentence premise** in `ADVENTURE.md`. GM intent and the player-facing briefing are not the contract. False intel is legal if the real problem is already in the starting state and the end states still answer the premise.
- **Pass/fail, not a rank.** Three rows with evidence. Fail any row, or omit the logic summary after a pass, and do not compile `RUN.md` as ready. The 120-point total and rank weights stay unchanged. A high numeric score with a failed coherence row is still not ready.
- **Causal reachability.** Each essential story point must be reachable from predetermined truths plus player decisions. Nothing important exists only because the plot needs it. Order stays flexible. This is not a named cause-and-effect script and not a calendar-only consistency check.
- **Evidence table plus logic summary.** A bare checkbox is not enough. Each row cites prep. After all three pass, write the logic summary. If any row fails, write the break in Evidence and skip the summary.
- **Operation Hinterland is in scope.** Fill the new block on that adventure in the same implementation pass. Re-score only coherence. Do not reopen the 98/120 unless that pass finds a real coherence break.

## Architecture

The scored adventure `QUALITY.md` is the source of truth for the check. Policy files point at it. `plot.md` is evidence, not a second audit.

| File | Change |
|---|---|
| `templates/adventure/QUALITY.md` | Add **Coherence (prep)** after the five-beat map and before the ranked checklist. |
| `GM.md` | One required-review question; one compile note that a failed or missing coherence block blocks ready compile. |
| `templates/adventure/ADVENTURE.md` | Pre-compilation checkbox: three-row check passed and logic summary present. |
| `templates/adventure/SKELETON.md` and `templates/adventure/RUN.md` | Compile checklist: coherence passed and logic summary present. |
| `HOW_TO_USE.md`, `README.md`, `adventures/README.md` | Mention the coherence block in existing “score QUALITY.md” lines. Extend the score prompt in `HOW_TO_USE.md`. |
| `adventures/operation-hinterland/QUALITY.md` | Fill the block, including a pass-only logic summary if the three rows pass. |
| `adventures/operation-hinterland/ADVENTURE.md` | Tick the new pre-compilation checkbox. |
| `adventures/operation-hinterland/RUN.md` | Compile checklist only: coherence passed. Do not rewrite story points. |

No new section in `plot.md` or `templates/adventure/plot.md`. Do not add a duplicate of the three rows to the existing Warning signs list.

## Coherence (prep) block

Place this in the QUALITY template so beginning / middle / end is read before the 0–5 ranks.

Copy the one-sentence premise from `ADVENTURE.md` at the top of the block. That sentence is the contract.

### Three-row table

| Check | Pass? | Evidence |
|---|---|---|
| Beginning with problems | yes/no | The starting state already contains the premise’s problem. The job does not appear only as a later reveal, and the opening is not unrelated trouble the premise never named. |
| Causal reachability | yes/no | Each essential story point is reachable from predetermined truths plus player decisions. Nothing important exists only because the plot needs it. Order stays flexible. |
| Ending answers the premise | yes/no | End states succeed, partly succeed, or fail that same job. They do not answer a different mission or require a scripted last scene to count. |

**Evidence rule:** a row passes only if Evidence cites actual prep: premise, truths, starting state, essential story points, and end states, in `ADVENTURE.md` and/or `plot.md` as the adventure uses them. “It feels coherent” is not evidence. An adventure that has no `plot.md` still fills this block from `ADVENTURE.md`.

**Pass?** is `yes` or `no`, not a 0–5 score.

### Fail conditions

- **Beginning:** the premise’s problem is not in the starting state; the job appears only after a later scene; or the opening is unrelated trouble the premise never named.
- **Reachability:** an essential story point exists only because the plot needs it; it cannot be reached from a truth plus a player decision; or the only way forward is one scripted path.
- **Ending:** end states resolve a different job than the premise, leave the premise’s job unaddressed, or require a scripted last scene to count.

### Not fails

False intel; optional dummy sites; player-chosen order; multiple independent vectors to the same essential piece; a climax situation that is “whichever second objective” rather than one unique room.

### Logic summary (only if all three pass)

If any row is `no`, do not write this section. Record the break in Evidence and repair before compile.

If all three are `yes`, write a short causal sketch. Parallel pieces stay parallel. Write “after learning B” only when C actually depends on B. Do not write a visit order.

```text
Premise job: <one sentence>

Problems already in play:
- ...

Reachable paths:
- <essential piece A> via <independent vector(s)>
- <essential piece B> via <independent vector(s)>
- <piece C> after learning B, via <vector(s)>   (only if C actually depends on B)

Conclusion: end states agree with these paths. This is not a visit order.
```

## Compile and review gates

Treat a missing block, a failed row, or a missing logic summary after a pass as blocking ready compile, the same way an unscored `QUALITY.md` already blocks it.

- **`GM.md` required review:** Has Coherence (prep) been filled, and did any row fail? If a row failed, or the logic summary is missing after a pass, do not compile as ready.
- **`GM.md` quality-gate paragraph:** keep maximum 120. Add that coherence is a separate pass/fail and can block compile regardless of the numeric band.
- **Pre-compilation (`ADVENTURE.md`):** `- [ ] Coherence (prep): three rows passed and logic summary present.`
- **Compile checklist (`SKELETON.md`, `RUN.md`):** `- [ ] Coherence (prep) passed; logic summary present in QUALITY.md.`

Ready still means numeric band (ready ≥ 100, or 80–99 with named repairs) **and** coherence passed.

## Hinterland first fill

Fill Operation Hinterland in the same pass. Use the adventure’s one-sentence premise as the contract. Expected shape if the rows pass (implementation may tighten wording; do not treat this as locked table text):

```text
Premise job: kill any two of three hydra heads so this station cannot keep helping the southern front.

Problems already in play:
- live hydra (board, loft, books)
- Ward’s pack is stale (wrong DZ, Rathaus as false head)
- short winter night, thin garrison

Reachable paths:
- board via Altrathausplatz (independent of the dummy)
- loft via Grüner Turm / north-wall aerial (independent)
- books via Brandt / Nördlinger (independent)
- dummy Rathaus is a pressure and a twist, not a required path; cutting it does not count
- two of three required; wounded hydra can still scream

Conclusion: end states agree with these paths (hydra dead or not). Order is player-chosen. This is not a visit order.
```

Do not rewrite `plot.md` or story points unless the check finds a real break. Do not change the 98/120 unless a coherence row fails.

## Out of scope

- Session recaps, played history, and canon promotion.
- Changing the 120-point weights or adding an 11th ranked item.
- Scoring GM intent or the player-facing briefing as the contract.
- A new `plot.md` coherence audit or a visit-order script.
- Forcing a unique climax location, explosive opening heat, or extra subsystems.
- Other adventures besides Operation Hinterland.
- Reproducing long copyrighted rules or adventure text.
