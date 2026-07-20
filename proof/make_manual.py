#!/usr/bin/env python3
"""User-approved fixes for pending judgment calls (capitalization/US + names)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = json.load(open(os.path.join(HERE, "..", "cards.original.json")))  # list, index by position

OPS = [
 (79 ,"Person",[("Lector","Lecter","real name is Hannibal Lecter")]),
 (107,"Text",  [("a us Department","a US Department","small-caps US")]),
 (256,"Text",  [("student Imitating","student imitating","capital-I mid-sentence")]),
 (290,"Text",  [("in calcutta","in Calcutta","proper noun")]),
 (292,"Text",  [("George In Of Mice","George in Of Mice","capital-I mid-sentence")]),
 (295,"Person",[("The Obermensch","The Übermensch","OCR of Ü as O; Nietzsche term")]),
 (323,"Person",[("Pharell","Pharrell","rapper is Pharrell Williams")]),
 (330,"Text",  [("of us\nrespondents","of US\nrespondents","small-caps US")]),
]
out=[]
for i,field,reps in OPS:
    original=src[i][field]; corrected=original; changes=[]
    for frm,to,note in reps:
        assert frm in corrected, f"card {i}: not found {frm!r}"
        corrected=corrected.replace(frm,to,1); changes.append({"from":frm,"to":to,"note":note})
    assert original.count("\n")==corrected.count("\n"), f"card {i}: newline count changed"
    out.append({"i":i,"field":field,"corrected":corrected,"changes":changes,"uncertain":False})
json.dump(out,open(os.path.join(HERE,"corr_manual.json"),"w"),ensure_ascii=False,indent=1)
print(f"corr_manual.json: {len(out)} approved fixes")
