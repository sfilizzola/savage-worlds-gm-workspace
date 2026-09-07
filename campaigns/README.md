# Campaigns

Each subdirectory `campaigns/<campaign-slug>/` owns **this table's** linked play: campaign-wide context (`CAMPAIGN.md`), campaign-local canon (`world/`), canonical party sheets (`characters/`), and **child adventure folders**.

Child adventures are ordinary adventure directories (each with `ADVENTURE.md`). They sit **directly beside** `world/` and `characters/`, not nested under them.

Standalone one-shots and other unsplit single-folder units remain under `adventures/<slug>/`. Do not put a linked campaign's nights there.

## Start

Copy `templates/campaign/` to `campaigns/<campaign-slug>/`. Complete `CAMPAIGN.md` before adding child adventures. Then copy `templates/adventure/` (except `SKELETON.md`) into `campaigns/<campaign-slug>/<adventure-slug>/` for each night or arc chapter.

## Suggested directory

```text
campaigns/<campaign-slug>/
├── CAMPAIGN.md
├── characters/          # canonical party .md sheets + print/chars.json
├── world/               # this table's evolving canon
│   ├── WORLD.md
│   ├── locations/
│   ├── factions/
│   ├── npcs/
│   └── lore/
├── <adventure-slug>/    # child adventure (ADVENTURE.md, QUALITY.md, RUN.md, …)
└── <another-slug>/
```

`CAMPAIGN.md` is configuration and indexes. It is not a table `RUN.md`. Campaigns have no `QUALITY.md`; score and compile those artifacts on each child adventure.

Root `world/` remains setting-wide. Put facts that are true only for this table in this campaign's `world/`.
