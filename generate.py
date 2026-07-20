#!/usr/bin/env python3
"""
Monikers card generator
========================
Builds print-ready PDFs from cards.json where **each card is its own page**,
sized for a printing agency to produce physical poker-size playing cards.

Page size : 69 x 94 mm  =  63 x 88 mm poker card (trim)  +  3 mm bleed all round.
Fonts     : official Gotham Rounded (Medium=names, Book=clue text, Bold=points),
            embedded from ./fonts as base64 so they travel inside the PDF.
Rendering : HTML -> PDF via headless Google Chrome (embeds .otf cleanly and gives
            precise control over the layout / bleed).

Outputs (in ./out):
    fronts.pdf   476 pages, one card front per page
    back.pdf     1 page, the shared red "MONIKERS faces" card back (full bleed)

Usage:
    python3 generate.py test     # 9-card sample  -> out/fronts_test.pdf
    python3 generate.py fronts    # all fronts      -> out/fronts.pdf
    python3 generate.py back       # card back        -> out/back.pdf
    python3 generate.py all        # fronts + back
"""
import json, os, re, base64, html, sys, subprocess

HERE     = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
ASSETS   = os.path.join(HERE, "assets")
OUT      = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CARDS  = json.load(open(os.path.join(HERE, "cards.json")))

# ---- point value -> official color -------------------------------------
POINT_COLOR = {1: "#4ABE9F", 2: "#00B5EF", 3: "#8769AE", 4: "#F0533F"}

# ---- official fonts (embedded as base64) -------------------------------
FONT_FILES = {
    "name": "gothamrnd_medium.otf",   # card names
    "body": "gothamrnd_book.otf",     # clue / description text
    "bold": "gothamrnd_bold.otf",     # point number
}

def font_face_css():
    faces = []
    for role, fname in FONT_FILES.items():
        path = os.path.join(FONT_DIR, fname)
        if not os.path.exists(path):
            print(f"!! missing font: {path}", file=sys.stderr)
            continue
        b64 = base64.b64encode(open(path, "rb").read()).decode()
        faces.append(
            f"@font-face{{font-family:'GR-{role}';"
            f"src:url(data:font/otf;base64,{b64}) format('opentype');}}"
        )
    return "\n".join(faces)

FONT_CSS = font_face_css()

# ---- text cleanup -------------------------------------------------------
def clean(s):
    """Collapse the OCR hard-wraps in the source data into flowing text."""
    s = s.replace("\r", "")
    s = re.sub(r"\s*\n\s*", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return html.escape(s)

def clean_name(s):
    """Keep the source's intentional line breaks in the name (matches the
    official card wrapping, e.g. 'A Russian' / 'Nesting Doll')."""
    parts = [html.escape(re.sub(r"\s+", " ", p).strip())
             for p in s.replace("\r", "").split("\n") if p.strip()]
    return "<br>".join(parts)

# ---- one card's HTML ----------------------------------------------------
def card_html(c):
    name  = clean_name(c["Person"])
    text  = clean(c["Text"])
    pts   = int(c["Points"])
    genre = html.escape((c.get("Genre") or "").upper())
    color = POINT_COLOR.get(pts, "#333333")
    label = "POINT" if pts == 1 else "POINTS"
    return f"""
    <section class="page">
      <div class="card">
        <div class="top">
          <div class="name">{name}</div>
          <div class="clue">{text}</div>
        </div>
        <div class="bottom">
          <div class="dots"></div>
          <div class="genre" style="color:{color}">{genre}</div>
          <div class="dome" style="background:{color}">
            <div class="num">{pts}</div>
            <div class="plabel">{label}</div>
          </div>
        </div>
      </div>
    </section>"""

FRONT_CSS = f"""
{FONT_CSS}
@page {{ size: 69mm 94mm; margin: 0; }}
* {{ box-sizing:border-box; -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
html,body {{ margin:0; padding:0; }}
.page {{ width:69mm; height:94mm; page-break-after:always; background:#ffffff; }}
.card {{
  position:relative; width:69mm; height:94mm; background:#fff;
  padding:12mm 9mm 8mm 9mm;          /* 3mm bleed + ~6mm safe inset */
  display:flex; flex-direction:column;
}}
.top {{ flex:1 1 auto; text-align:center; }}
.name {{
  font-family:'GR-name','Futura',sans-serif; font-weight:500;
  font-size:13pt; line-height:1.12; color:#2b2b2b; letter-spacing:.2pt;
}}
.clue {{
  font-family:'GR-body','Avenir',sans-serif; font-weight:400;
  font-size:7.6pt; line-height:1.36; color:#5b5b5b; text-align:left; margin-top:6mm;
}}
.bottom {{ flex:0 0 auto; text-align:center; margin-bottom:19mm; }}
.dots {{ width:22mm; height:0; margin:0 auto 3mm auto; border-top:1.4pt dotted #bcbcbc; }}
.genre {{
  font-family:'GR-name','Futura',sans-serif; font-weight:500;
  font-size:6.4pt; letter-spacing:2.2pt; text-transform:uppercase; margin-bottom:2.5mm;
}}
/* point container: anchored to the card's bottom edge, bleeding off it so the
   colour reaches the very edge after trimming. Rounded top, flush flat bottom. */
.dome {{
  position:absolute; left:50%; bottom:0; transform:translateX(-50%);
  width:16.5mm; height:19mm;
  border-radius:8.25mm 8.25mm 0 0;   /* = half width -> clean semicircular top */
  color:#fff; display:flex; flex-direction:column;
  align-items:center; justify-content:flex-start; padding-top:2.6mm;
}}
.num {{ font-family:'GR-bold','Futura',sans-serif; font-weight:700; font-size:15pt; line-height:1; }}
.plabel {{ font-family:'GR-name','Futura',sans-serif; font-weight:500;
          font-size:3.6pt; letter-spacing:1.4pt; margin-top:.8mm; }}
"""

def build_fronts_html(cards, path):
    body = "\n".join(card_html(c) for c in cards)
    open(path, "w").write(
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{FRONT_CSS}</style></head><body>{body}</body></html>"
    )
    return path

def build_back_html(path):
    img = os.path.join(ASSETS, "card-back.webp")
    b64 = base64.b64encode(open(img, "rb").read()).decode()
    css = """
@page { size: 69mm 94mm; margin: 0; }
html,body { margin:0; padding:0; }
* { -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { width:69mm; height:94mm;
        background-image:url(data:image/webp;base64,%s);
        background-size:cover; background-position:center; }
""" % b64
    open(path, "w").write(
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{css}</style></head><body><div class='page'></div></body></html>"
    )
    return path

def render_pdf(html_path, pdf_path):
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", html_path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    return pdf_path

# ---- entrypoint ---------------------------------------------------------
if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    if mode == "test":
        h = build_fronts_html(CARDS[:5], os.path.join(OUT, "fronts_test.html"))
        render_pdf(h, os.path.join(OUT, "fronts_test.pdf"))
        print("wrote out/fronts_test.pdf (5 cards)")
    if mode in ("fronts", "all"):
        h = build_fronts_html(CARDS, os.path.join(OUT, "fronts.html"))
        render_pdf(h, os.path.join(OUT, "fronts.pdf"))
        print(f"wrote out/fronts.pdf ({len(CARDS)} cards)")
    if mode in ("back", "all"):
        h = build_back_html(os.path.join(OUT, "back.html"))
        render_pdf(h, os.path.join(OUT, "back.pdf"))
        print("wrote out/back.pdf (1 page)")
