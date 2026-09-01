# Call letters — print

Real-life invitations. Not table canon, not a briefing, not session history.

Print one A4 per envelope. **DATE / TIME** is printed: 14.11.2026 at 1400 hours.

| File | Who |
|---|---|
| `letter-keene.pdf` | 1st Lt. Jack Keene |
| `letter-krajewski.pdf` | Sgt. Tomasz Krajewski |
| `letter-vasseur.pdf` | Sgt. Hélène Vasseur |
| `letter-lang.pdf` | Cpl. Beatrice Lang |

Rebuild:

```text
python3 build_letters.py --who all --pdf
```

`--who` is `keene` | `krajewski` | `vasseur` | `lang` | `all`.  
Date/time is in `build_letters.py` (`WHEN`). Pass `--when` only to override.

Source text: `../letter-*.md`.
