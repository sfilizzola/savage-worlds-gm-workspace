# Call letters — print

Real-life invitations. Not table canon, not a briefing, not session history.

Print one A4 per envelope. Leave the **DATE / TIME** line blank and fill it by hand.

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
Do not pass `--when` unless you want the date typed in.

Source text: `../letter-*.md`.
