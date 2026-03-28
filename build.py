#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "jinja2",
# ]
# ///
"""
Build script — renders Jinja2/Nunjucks-compatible templates to static HTML.

Usage:
  uv run build.py
"""
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '_templates')),
    autoescape=select_autoescape(['html']),
    trim_blocks=True,
    lstrip_blocks=True,
)

# ── Contact ─────────────────────────────────────────────────────────────────
PHONE         = "+237699044427"           # used in tel: links and JSON-LD
PHONE_DISPLAY = "+237 6 99 04 44 27"      # displayed to the user
EMAIL         = "hello@proxima.cm"

WA_NUM = PHONE.lstrip("+")               # digits only for wa.me URLs
WA     = f"https://wa.me/{WA_NUM}?text=" # base URL for WhatsApp messages
WA_TEL = f"https://wa.me/{WA_NUM}"       # footer WhatsApp link (no message)

PAGES = [
    {
        'template': 'pages/index.html',
        'output':   'index.html',

        # ── Contact info ────────────────────────────────────────
        'phone':         PHONE,
        'phone_display': PHONE_DISPLAY,
        'phone_url':     f"tel:{PHONE}",
        'wa_tel':        WA_TEL,
        'email':         EMAIL,

        # ── Nav + floating button ────────────────────────────────
        'wa_header_url':                WA + "Bonjour%2C%20j%27aimerais%20avoir%20les%20services%20de%20Proxima%20Technologies",
        'wa_header_label':              "WhatsApp",
        'wa_float_url':                 WA + "Bonjour%2C%20j%27aimerais%20avoir%20les%20services%20de%20Proxima%20Technologies",
        'wa_float_tip':                 "Écrivez-nous !",

        # ── Hero ────────────────────────────────────────────────
        'wa_hero':                      WA + "Bonjour%2C%20j%27aimerais%20avoir%20les%20services%20de%20Proxima%20Technologies",
        'wa_hero_label':                "Écrivez-nous sur WhatsApp",

        # ── Produits ────────────────────────────────────────────
        'wa_commerce':                  WA + "Bonjour%2C%20j%27aimerais%20impl%C3%A9menter%20Odoo%20pour%20ma%20gestion%20commerciale",
        'wa_commerce_label':            "Demander une démo",
        'wa_education':                 WA + "Bonjour%2C%20j%27aimerais%20avoir%20votre%20logiciel%20de%20gestion%20des%20frais%20de%20scolarit%C3%A9",
        'wa_education_label':           "Demander une démo",

        # ── AlphaDSF tarifs ─────────────────────────────────────
        'wa_alphadsf_community':        WA + "Bonjour%2C%20pouvez-vous%20m%27envoyer%20une%20version%20gratuite%20de%20AlphaDSF%20%3F",
        'wa_alphadsf_community_label':  "Commander",
        'wa_alphadsf_standard':         WA + "Bonjour%2C%20je%20veux%20AlphaDSF%20Standard%20%C3%A0%20150%20000%20FCFA",
        'wa_alphadsf_standard_label':   "Commander",
        'wa_alphadsf_premium':          WA + "Bonjour%2C%20je%20veux%20AlphaDSF%20Premium%20%C3%A0%20300%20000%20FCFA",
        'wa_alphadsf_premium_label':    "Commander",

        # ── CTA final ────────────────────────────────────────────
        'wa_cta':                       WA + "Bonjour%2C%20j%27aimerais%20avoir%20les%20services%20de%20Proxima%20Technologies",
        'wa_cta_label':                 "Écrire sur WhatsApp",
    },
]

output_dir = os.path.dirname(__file__)

for page in PAGES:
    tmpl = env.get_template(page['template'])
    ctx  = {k: v for k, v in page.items() if k not in ('template', 'output')}
    html = tmpl.render(**ctx)
    out  = os.path.join(output_dir, page['output'])
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓  {page['output']}")

print("\nAll pages built. Open index.html to preview.")
