# Monikers Card Generator — Project Directives

A small Python tool that turns `cards.json` (476 Monikers cards) into
print-ready PDFs, one card per page, for a printing agency to produce physical
poker-size playing cards. It is a personal, non-commercial print aid: Monikers
is CC BY-NC-SA 4.0 (Alex Hague, Justin Vickers, Max Temkin), and the card data
originally came from github.com/yene/Monikers.

## Hard constraints

- **Print geometry is fixed:** page 69 x 94 mm = 63 x 88 mm poker trim + 3 mm
  bleed on every side. Keep text inside the safe inset (card padding
  `12mm 9mm 8mm 9mm`). The point "dome" must bleed off the bottom edge so the
  colour reaches the trimmed edge.
- **Point colours are fixed:** 1 = `#4ABE9F`, 2 = `#00B5EF`, 3 = `#8769AE`,
  4 = `#F0533F` (`POINT_COLOR` in `generate.py`).
- **Never commit the fonts.** Gotham Rounded is commercial (Hoefler & Co).
  `.gitignore` excludes `fonts/*.otf` and `fonts/*.ttf`; keep it that way.
- **Keep the licence non-commercial** and keep the credits in `README.md`.
- **`cards.original.json` is pristine.** Never edit it; all corrections are
  derived from it.

## Architecture

```
generate.py            cards.json -> HTML -> PDF via headless Google Chrome
apply_corrections.py   cards.original.json + proof/corr_*.json -> cards.json + diff.md
cards.json             corrected deck (source of truth for generation)
cards.original.json    OCR-scanned original, untouched
diff.md                review log of every applied / uncertain / rejected correction
assets/card-back.webp  shared card-back artwork
fonts/                 place licensed gothamrnd_{medium,book,bold}.otf here (see fonts/README.md)
out/                   fronts.pdf (476 pages) and back.pdf (1 page) are committed
proof/                 proofreading intermediates: corr_*.json, make_corr5.py, make_manual.py
```

`generate.py` builds one HTML page per card (name, clue, dotted rule, genre,
point dome), embeds fonts and the card back as base64 data URIs, and prints
with Chrome `--headless --print-to-pdf`. Chrome is used because it embeds the
.otf fonts cleanly and gives precise control over layout and bleed. Card schema:
`Person` (name, intentional line breaks kept), `Text` (clue; OCR hard-wraps
collapsed by `clean()`), `Genre`, `Points` (1-4).

## Commands

```
python3 generate.py test      # first 5 cards -> out/fronts_test.pdf
python3 generate.py fronts    # all fronts    -> out/fronts.pdf
python3 generate.py back      # card back     -> out/back.pdf
python3 generate.py all       # fronts + back
python3 apply_corrections.py  # rebuild cards.json + diff.md from corrections
```

No arguments defaults to `test`. There is no test suite, linter or deploy; the
check is to open the PDF. Requirements: Python 3 and Google Chrome. README also
lists PyMuPDF/Pillow for previews; `generate.py` does not import them.

## Proofreading workflow

The source text was OCR-scanned. Corrections are data, not hand edits:

1. Each `proof/corr_*.json` is a list of `{i, field, corrected, changes,
   uncertain}` entries, where `i` indexes `cards.original.json` and `field` is
   `Person` or `Text`.
2. `apply_corrections.py` applies all of them to a copy of the original, with
   guardrails: the newline count must not change and similarity must stay
   >= 0.80, so a fix cannot silently paraphrase a card. It rewrites `cards.json`
   and `diff.md`.
3. Current result: 183 applied, 76 flagged uncertain, 0 rejected. Some of the
   game's own wording quirks were left intact on purpose.

To fix a card, add an entry to a `corr_*.json` file (or a small script like
`proof/make_manual.py`, which holds user-approved judgement calls) and rerun
`apply_corrections.py`. Editing `cards.json` directly is lost on the next run.

## Conventions

- Plain Python 3 scripts, stdlib only in `generate.py` and
  `apply_corrections.py`; paths are resolved relative to the script (`HERE`).
- Layout lives in the `FRONT_CSS` string in `generate.py`, in mm and pt units.
- Only one commit exists, so there is no established commit style; use short
  imperative subjects.

## Gotchas

- The Chrome path is hardcoded for macOS
  (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`). Change
  `CHROME` to run elsewhere. Chrome output is discarded, so a failure shows
  only as a non-zero exit.
- Missing fonts are not fatal: `generate.py` prints `!! missing font` and falls
  back to Futura / Avenir / system sans. Check for that warning before sending
  PDFs to a printer.
- The `generate.py` docstring says `test` builds 9 cards; the code builds 5.
- `proof/batch_*.json` is gitignored, so `proof/make_corr5.py` cannot be rerun
  from a clean clone. Its output `corr_5.json` is committed.
- `out/*.html`, `out/*.png` and `out/fronts_test.pdf` are gitignored;
  `out/fronts.pdf` and `out/back.pdf` are committed, so regenerate them after
  any card or layout change.
- Some `Genre` values are credit lines from the original cards
  ("CARD BY ...", "NAME BY ..."), not categories. They are printed as-is.

## Current state and next steps

Complete for its purpose: all 476 fronts and the shared back are generated and
committed, ready to send to a printer (for example MakePlayingCards or
DriveThruCards) with `back.pdf` as the single back. The 76 "uncertain" entries in
`diff.md` are left for human review. No roadmap or TODOs are recorded in the
repo.
