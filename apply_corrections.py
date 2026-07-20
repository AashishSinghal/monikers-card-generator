#!/usr/bin/env python3
"""
Apply the proofreaders' OCR corrections back INTO cards.json.

- Reads the pristine original from cards.original.json.
- Reads every proof/corr_*.json produced by the proofreading agents.
- Validates each correction is a light-touch edit (same number of newlines,
  modest character-level change) so no card gets silently paraphrased.
- Writes the corrected deck to cards.json.
- Writes a human-review diff to diff.md (confident fixes + uncertain flags).
"""
import json, os, glob, difflib

HERE = os.path.dirname(os.path.abspath(__file__))
orig = json.load(open(os.path.join(HERE, "cards.original.json")))
cards = json.loads(json.dumps(orig))   # deep copy to mutate

corr = []
for f in sorted(glob.glob(os.path.join(HERE, "proof", "corr_*.json"))):
    try:
        corr.extend(json.load(open(f)))
    except Exception as e:
        print(f"!! could not read {f}: {e}")

applied, flagged, rejected = [], [], []

def inline_diff(a, b):
    """word-level inline diff -> markdown with ~~del~~ and **add**."""
    sm = difflib.SequenceMatcher(a=a.split(), b=b.split())
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        aw = " ".join(a.split()[i1:i2]); bw = " ".join(b.split()[j1:j2])
        if tag == "equal": out.append(aw)
        elif tag == "delete": out.append(f"~~{aw}~~")
        elif tag == "insert": out.append(f"**{bw}**")
        else: out.append(f"~~{aw}~~ **{bw}**")
    return " ".join(x for x in out if x)

for c in corr:
    i, field, new = c.get("i"), c.get("field"), c.get("corrected")
    if i is None or field not in ("Person", "Text") or new is None:
        rejected.append((c, "malformed entry")); continue
    old = orig[i][field]
    # guardrail: never let a "fix" rewrite the whole thing
    if old.count("\n") != new.count("\n"):
        rejected.append((c, "newline count changed")); continue
    ratio = difflib.SequenceMatcher(None, old, new, autojunk=False).ratio()
    if ratio < 0.80 and old != new:
        rejected.append((c, f"too different (sim={ratio:.2f})")); continue
    changed = old != new
    if changed:
        cards[i][field] = new
        applied.append((i, field, old, new, c.get("changes", [])))
    if c.get("uncertain"):
        flagged.append((i, field, old, new, c.get("changes", [])))

json.dump(cards, open(os.path.join(HERE, "cards.json"), "w"),
          ensure_ascii=False, indent=2)

# ---- diff.md ----
lines = ["# Monikers OCR proofreading — review\n",
         f"- Corrections applied: **{len(applied)}**",
         f"- Uncertain (needs your eyes): **{len(flagged)}**",
         f"- Rejected by guardrail (left as original): **{len(rejected)}**\n",
         "Names are shown as `Person`; clue text as `Text`. "
         "~~struck~~ = removed, **bold** = added.\n",
         "---\n## Applied corrections\n"]
def nm(i): return orig[i]["Person"].replace("\n", " ")
for i, field, old, new, ch in sorted(applied):
    lines.append(f"**#{i} · {nm(i)} · {field}**  ")
    lines.append(inline_diff(old.replace(chr(10)," "), new.replace(chr(10)," ")))
    for x in ch:
        lines.append(f"  - `{x.get('from','')}` → `{x.get('to','')}` — {x.get('note','')}")
    lines.append("")
if flagged:
    lines.append("---\n## Uncertain — please confirm\n")
    for i, field, old, new, ch in sorted(flagged):
        lines.append(f"**#{i} · {nm(i)} · {field}**  ")
        for x in ch:
            lines.append(f"  - `{x.get('from','')}` → `{x.get('to','')}` — {x.get('note','')}")
        lines.append("")
if rejected:
    lines.append("---\n## Rejected by guardrail (kept original)\n")
    for c, why in rejected:
        lines.append(f"- #{c.get('i')} {c.get('field')}: {why}")

open(os.path.join(HERE, "diff.md"), "w").write("\n".join(lines))
print(f"applied={len(applied)} uncertain={len(flagged)} rejected={len(rejected)}")
print("wrote cards.json + diff.md")
