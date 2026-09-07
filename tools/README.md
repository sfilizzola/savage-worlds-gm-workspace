# Tools

Workspace utilities that are not adventure-specific.

| Tool | What it does |
|---|---|
| [`print-sheets/`](print-sheets/) | SWADE pregen **sheet printer** (HTML/PDF). Not a character generator. |
| [`print-run/`](print-run/) | Adventure **`RUN.md` printer** (A4 two-column HTML/PDF). Not a compiler. |

Both tools read explicit input paths, so they work from either playable root:

- standalone adventure data: `adventures/<slug>/`;
- a campaign night's adventure data: `campaigns/<campaign-slug>/<adventure-slug>/`;
- a campaign's canonical party: `campaigns/<campaign-slug>/characters/`.

Call letters and other table handouts stay with the adventure that owns them.
