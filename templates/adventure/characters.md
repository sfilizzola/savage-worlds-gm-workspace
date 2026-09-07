# Characters

The adventure configuration determines which sections are active.

## Party assumptions

- Rank:
- Player count:
- Allowed character sources:
- Required competencies without requiring one specific skill/Edge:
- Shared reason to engage:

## Pregenerated PCs

For each pregen include concept, complete source-verified game statistics, gear, personal objective, connection to the mission, connections to other PCs, and a compact table-use summary. Cite rules sources for non-obvious mechanics.

Print A4 sheets with the workspace tool [`tools/print-sheets/`](../../tools/print-sheets/README.md) (HTML/PDF printer, not a generator). Keep one `.md` file per pregen as the mechanical source of truth. Put the print extract in `characters/print/chars.json` and rebuild:

```text
python3 tools/print-sheets/render.py adventures/<slug>/characters/print/chars.json --pdf
```

In a campaign, the party is canonical at the campaign root, so print from there instead:

```text
python3 tools/print-sheets/render.py campaigns/<campaign-slug>/characters/print/chars.json --pdf
```

Either way the sheets are written beside the `chars.json` you passed, in that same character `print/` directory.

If this file belongs to a child adventure under `campaigns/`, keep it to night hooks and links to the campaign's canonical sheets. Do not copy full mechanical sheets down into the child.

### <Name>

- Concept:
- Hook:
- Personal stake:
- Party connections:
- Statistics:
- Source verification:
- Table notes:

## Player-supplied PC intake

- [ ] Correct Rank and advancement assumptions.
- [ ] Uses allowed books/modules.
- [ ] Has a reason to accept or remain in the premise.
- [ ] Gear fits the setting and historical requirements.
- [ ] Powers, Edges, and special abilities were verified.
- [ ] No essential clue or plot beat depends on this PC alone.
- [ ] Character-specific spotlight opportunity identified.

## Early removal mitigation

- Opening risks that could hard-remove a PC:
- Telegraphing or recovery built into those risks:
- Reserve pregen or allied character:
- Fictional entry point for replacement:
- Procedure for capture/separation without sidelining the player:

## Later lethality

State when the adventure's danger becomes fully lethal and how the fiction communicates that transition. This is risk communication, not immunity.

