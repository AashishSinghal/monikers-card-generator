#!/usr/bin/env python3
"""Hand-proofread corrections for batch 5 (cards 300-359).
Encoded as targeted find->replace ops so `corrected` differs from the source
only at these exact spots. Emits corr_5.json in the same schema as the agents."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = {c["i"]: c for c in json.load(open(os.path.join(HERE, "batch_5.json")))}

# (i, field, [(from, to, note)], uncertain, [uncertain_notes])
OPS = [
 (301,"Text",[("id losyncratlc","idiosyncratic","OCR l/i + stray space"),
              ("del Ivery","delivery","OCR split + I/l"),
              ('Babooshka.\n· One','Babooshka."\nOne',"stray · stood in for closing quote")],False,[]),
 (302,"Person",[("A Cyberbu lly","A Cyberbully","OCR stray space")],False,[]),
 (303,"Text",[("sti II not","still not","OCR split")],True,
       ["'Fanke' is likely the character 'Tobias Fünke' (left unchanged — confirm)"]),
 (311,"Text",[("pederast In the","pederast in the","capital-I for i mid-sentence")],False,[]),
 (313,"Text",[("yeah I I shake","yeah I shake","OCR doubled I")],True,
       ["'Fairbrassin brothers' is likely 'Fairbrass brothers' (left unchanged — confirm)"]),
 (315,"Text",[("late><","latex","OCR >< read for x"),
              ("difficu It","difficult","OCR split"),
              ("><-ray","x-ray","OCR >< read for x")],False,[]),
 (316,"Text",[("One of the the three","One of the three","duplicated word"),
              ("an e><ecutive","an executive","OCR >< read for x")],False,[]),
 (317,"Text",[("Deschanel In everything","Deschanel in everything","capital-I for i")],False,[]),
 (319,"Text",[("Japan. its preparation","Japan. Its preparation","lost capital after period")],False,[]),
 (321,"Text",[('purses.•','purses."',"stray • stood in for closing quote")],False,[]),
 (323,"Person",[],True,["'Pharell' is likely 'Pharrell' (Williams) (left unchanged — confirm)"]),
 (324,"Text",[("Tobias FOnke","Tobias Fünke","OCR of 'Fünke' (Arrested Development)")],False,[]),
 (328,"Text",[("networking sitebefore","networking site before","words joined by scan")],False,[]),
 (330,"Text",[],True,["'32% of us respondents' — 'us' is likely small-caps 'US' (left unchanged — confirm)"]),
 (334,"Text",[("former us Congressman","former US Congressman","small-caps US read as us")],False,[]),
 (336,"Text",[("used In reference","used in reference","capital-I for i")],False,[]),
 (340,"Text",[("wil I arrive","will arrive","OCR split")],False,[]),
 (344,"Text",[("President of the us,","President of the US,","small-caps US"),
              ("mouth\nIs clogged","mouth\nis clogged","capital-I for i")],False,[]),
 (351,"Text",[("slaves In the","slaves in the","capital-I for i"),
              ("afterl lfe","afterlife","OCR split + l")],False,[]),
 (352,"Person",[("E.Honda","E. Honda","missing space")],False,[]),
 (353,"Text",[("preppy yaung","preppy young","OCR a for o")],False,[]),
 (355,"Text",[],True,["'hives knows as colonies' likely 'known as' (left unchanged — confirm)"]),
 (357,"Text",[('serpent.•','serpent."',"stray • stood in for closing quote"),
              ("Hern~n Cort~s","Hernán Cortés","OCR ~ for accented á/é")],False,[]),
 (359,"Text",[('joy•\n','joy"\n',"stray • = closing quote"),
              ('ridiculous•\n','ridiculous"\n',"stray • = closing quote")],False,[]),
]

out = []
for i, field, reps, uncertain, unotes in OPS:
    original = src[i][field]
    corrected = original
    changes = []
    for frm, to, note in reps:
        assert frm in corrected, f"card {i}: substring not found: {frm!r}"
        corrected = corrected.replace(frm, to, 1)
        changes.append({"from": frm, "to": to, "note": note})
    for n in unotes:
        changes.append({"from": "", "to": "", "note": n})
    assert original.count("\n") == corrected.count("\n"), f"card {i}: newline count changed"
    out.append({"i": i, "field": field, "corrected": corrected,
                "changes": changes, "uncertain": uncertain})

json.dump(out, open(os.path.join(HERE, "corr_5.json"), "w"), ensure_ascii=False, indent=1)
print(f"corr_5.json: {len(out)} entries, "
      f"{sum(1 for o in out if o['corrected']!=src[o['i']][o['field']])} changed, "
      f"{sum(1 for o in out if o['uncertain'])} uncertain")
