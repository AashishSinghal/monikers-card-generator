# Monikers Card Generator

Generates **print-ready PDFs** of all 476 Monikers cards — one card per page —
for a printing agency to produce as physical poker-size playing cards.

Monikers is released under Creative Commons BY-NC-SA 4.0 (non-commercial), so
printing a personal copy is fine.

## Output (`out/`)
| File | Pages | What |
|------|-------|------|
| `fronts.pdf` | 476 | One card front per page |
| `back.pdf`  | 1   | Shared card back (red MONIKERS faces) |

**Page size:** 69 × 94 mm = **63 × 88 mm** poker card (trim) + **3 mm bleed** all around.
Point value → colour: 1 = teal `#4ABE9F`, 2 = blue `#00B5EF`, 3 = purple `#8769AE`, 4 = red `#F0533F`.
The point "dome" bleeds off the bottom edge so the colour runs to the trimmed edge.

### Sending to a printer
- Most agencies (MakePlayingCards, DriveThruCards, etc.) accept these directly.
- Give them `back.pdf` as the single shared back for every card.
- Fonts (Gotham Rounded) are embedded in the PDF; no need to send them.

## Rebuild
```
python3 generate.py test     # 5-card sample -> out/fronts_test.pdf
python3 generate.py fronts    # all fronts     -> out/fronts.pdf
python3 generate.py back       # card back       -> out/back.pdf
python3 generate.py all        # fronts + back
```
Requires: Python 3, `PyMuPDF`/`Pillow` (for previews), and Google Chrome
(headless print-to-pdf renders the HTML so the .otf fonts embed cleanly).

## Files
- `cards.json` — card data, **OCR-corrected** (source of truth).
- `cards.original.json` — pristine original (before proofreading).
- `diff.md` — every proofreading change, for review.
- `fonts/` — where to place Gotham Rounded (**not included** — commercial font; see `fonts/README.md`).
- `assets/card-back.webp` — the red card-back artwork.
- `proof/` — throwaway proofreading intermediates.

## Text proofreading
The source `cards.json` was OCR-scanned and had scan typos ("Shiba lnu",
"Bitcoln", etc.). 183 clear OCR errors were auto-fixed; a handful of the
game's own original wording quirks were deliberately left intact. See `diff.md`.

## Credits
- **Monikers** by Alex Hague, Justin Vickers & Max Temkin — <https://monikersgame.com>,
  released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
  This project is a non-commercial personal print aid.
- Card data (`cards.json`) originally sourced from [github.com/yene/Monikers](https://github.com/yene/Monikers).
