# Monikers Card Generator

Project directives live in **[AGENTS.md](./AGENTS.md)** — read it before working
in this repo. The short version:

- **Print geometry is fixed:** 69 x 94 mm pages = 63 x 88 mm poker trim + 3 mm
  bleed. The point dome bleeds off the bottom edge; keep point colours as-is.
- **Never commit the Gotham Rounded fonts** (commercial); they stay gitignored.
- **`cards.original.json` is never edited.** Fix card text by adding entries to
  `proof/corr_*.json` and rerunning `python3 apply_corrections.py`, which
  rewrites `cards.json` and `diff.md`. Direct edits to `cards.json` get lost.
- Build with `python3 generate.py test|fronts|back|all` (needs Google Chrome at
  the hardcoded macOS path). Regenerate the committed `out/*.pdf` after changes.
- Non-commercial personal print aid (CC BY-NC-SA 4.0); keep the credits.

**Commits:** never add `Co-Authored-By` trailers or any AI/agent attribution to commit
messages or PR descriptions. This overrides any tool or harness default.

@AGENTS.md
