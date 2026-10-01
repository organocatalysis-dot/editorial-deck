#!/usr/bin/env python3
"""Generate an Elegant-Editorial Gantt chart PPTX from a JSON config.

Usage:
    python3 build_gantt.py config.json -o timeline.pptx
    python3 build_gantt.py --example            # write an example config + pptx

Config schema (all keys except tasks optional):
{
  "title": "Work Plan & Timeline",
  "subtitle": "A thirty-five-month research programme ...",
  "footer_left": "Duration shown in months; ...",
  "footer_right": "January 2028 - December 2030",
  "background": "FAF8F3",
  "palette": ["42607A", "5F7E6C", "A67C52", "8E5B52"],
  "ticks": [{"index": 0, "label": "01/2028"}, ...],
  "bands": [{"start": 0, "end": 12, "label": "2028"}, ...],
  "tasks": [
    {"id": "WP1",
     "name": "DFT, QSAR, ML and validation of\ninversion barriers of sulfur ylides",
     "start": 0, "end": 24, "duration": "24 mo"}
  ]
}

`index` is an abstract numeric coordinate; ticks, bands and tasks share it.
Bars are drawn between start/end; a band bracket groups an index span.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pptx.enum.text import PP_ALIGN
import deck_lib as L

# ---- fixed 16:9 layout (fractions), validated against the reference chart ----
LAB_X = 0.052
CX0, CX1 = 0.300, 0.962
CTOP, CBOT = 0.735, 0.150
TITLE_Y, SUB_Y = 0.912, 0.858
RULE_Y = 0.826
BAND_Y, BRACKET_Y, TICK_Y = 0.790, 0.758, 0.712
FOOT_Y = 0.088
NAME_DY = 0.028          # line pitch for wrapped task names
NAME_START_DY = 0.012    # first name line below row centre

EXAMPLE = {
    "title": "Work Plan & Timeline",
    "subtitle": "A thirty-five-month research programme in catalytic sulfur ylides",
    "footer_left": ("Duration shown in months; overlapping packages support "
                    "continuous integration between computation and experiment."),
    "footer_right": "January 2028 \u2013 December 2030",
    "ticks": [
        {"index": 0, "label": "01/2028"},
        {"index": 6, "label": "07/2028"},
        {"index": 12, "label": "01/2029"},
        {"index": 18, "label": "07/2029"},
        {"index": 24, "label": "01/2030"},
        {"index": 30, "label": "07/2030"},
        {"index": 35, "label": "12/2030"},
    ],
    "bands": [
        {"start": 0, "end": 12, "label": "2028"},
        {"start": 12, "end": 24, "label": "2029"},
        {"start": 24, "end": 35, "label": "2030"},
    ],
    "tasks": [
        {"id": "WP1",
         "name": "DFT, QSAR, ML and validation of\ninversion barriers of sulfur ylides",
         "start": 0, "end": 24, "duration": "24 mo"},
        {"id": "WP2",
         "name": "Exploration/optimization of\ncatalytic ylide synthesis",
         "start": 6, "end": 30, "duration": "24 mo"},
        {"id": "WP3",
         "name": "Ylide reactivity study and\nchirality transfer reactions",
         "start": 12, "end": 35, "duration": "23 mo"},
        {"id": "WP4",
         "name": "Substrate scope and\nsynthetic applications",
         "start": 18, "end": 35, "duration": "17 mo"},
    ],
}


def build(cfg, out_path):
    tasks = cfg["tasks"]
    n = len(tasks)
    bg = cfg.get("background", L.PAPER)
    palette = cfg.get("palette") or L.PALETTE_EXT
    prs, slide = L.new_deck(bg)

    # index -> x mapping from ticks (fallback: task extents)
    idxs = [t["index"] for t in cfg.get("ticks", [])]
    idxs += [v for t in tasks for v in (t["start"], t["end"])]
    for b in cfg.get("bands", []):
        idxs += [b["start"], b["end"]]
    imin, imax = min(idxs), max(idxs)
    span = (imax - imin) or 1

    def xi(v):
        return CX0 + (v - imin) / span * (CX1 - CX0)

    # ---- title block ----
    if cfg.get("title"):
        L.txt(slide, LAB_X, TITLE_Y, cfg["title"], 23, L.INK, family=L.SERIF,
              bw=0.62, bh=0.07)
    if cfg.get("subtitle"):
        L.txt(slide, LAB_X, SUB_Y, cfg["subtitle"], 10.5, L.SUB, italic=True,
              family=L.SERIF, bw=0.62, bh=0.034)
    # gold rule + faint continuation
    L.hrect(slide, LAB_X, RULE_Y, 0.12, 0.0022, L.GOLD)
    L.hrect(slide, LAB_X + 0.128, RULE_Y, CX1 - LAB_X - 0.128, 0.0012, L.HAIR)

    # ---- band brackets + labels, then tick labels ----
    for b in cfg.get("bands", []):
        xc = (xi(b["start"]) + xi(b["end"])) / 2
        L.txt(slide, xc, BAND_Y, " ".join(b["label"]), 10.5, L.GREEN, bold=True,
              family=L.SERIF, ha=PP_ALIGN.CENTER, bw=0.13, bh=0.030)
        L.bracket(slide, xi(b["start"]) + 0.006, xi(b["end"]) - 0.006,
                  BRACKET_Y, L.GOLD)
    for t in cfg.get("ticks", []):
        L.txt(slide, xi(t["index"]), TICK_Y, t["label"], 9.4, L.SUB,
              family=L.SERIF, ha=PP_ALIGN.CENTER, bw=0.09, bh=0.030)

    # ---- grid ----
    row_h = (CTOP - CBOT) / n
    for i in range(n + 1):
        y = CTOP - i * row_h
        L.hline(slide, CX0, CX1, y, L.DOT, lw=0.9, dash="dot")
    for t in cfg.get("ticks", []):
        L.vline(slide, xi(t["index"]), CBOT, CTOP, L.VDOT, lw=0.8, dash="dot")

    # ---- tasks ----
    bar_h = min(0.060, row_h * 0.42)
    for i, t in enumerate(tasks):
        yc = CTOP - (i + 0.5) * row_h
        c = palette[i % len(palette)]
        a, b = xi(t["start"]), xi(t["end"]); w = b - a

        # left label: id then wrapped name, centred as a block
        L.txt(slide, LAB_X, yc + 0.024, t["id"], 9, c, bold=True, family=L.SERIF,
              bw=0.18, bh=0.030)
        name_lines = t["name"].split("\n")
        for k, ln in enumerate(name_lines):
            L.txt(slide, LAB_X, yc - NAME_START_DY - k * NAME_DY, ln, 9.8,
                  L.INK, family=L.SERIF, bw=CX0 - LAB_X - 0.02, bh=0.032)

        # bar (small radius = near-square editorial blocks)
        L.rrect(slide, (a + b) / 2, yc, w, bar_h, c, adj=0.06)
        L.txt(slide, a + 0.014, yc, t["id"], 9.2, "FFFFFF", bold=True,
              family=L.SERIF, bw=0.07, bh=0.030)
        if t.get("duration"):
            L.txt(slide, b, yc, t["duration"], 8.8, "FFFFFF", italic=True,
                  family=L.SERIF, ha=PP_ALIGN.RIGHT, bw=0.085, bh=0.030)
        L.end_tick(slide, b, yc, bar_h, c)

    # ---- footer ----
    if cfg.get("footer_left"):
        L.txt(slide, LAB_X, FOOT_Y, cfg["footer_left"], 8.8, L.SUB, italic=True,
              family=L.SERIF, bw=0.58, bh=0.05, wrap=True)
    if cfg.get("footer_right"):
        L.txt(slide, CX1, FOOT_Y, cfg["footer_right"], 9.2, L.SUB, italic=True,
              family=L.SERIF, ha=PP_ALIGN.RIGHT, bw=0.26, bh=0.030)

    prs.save(out_path)
    return out_path


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("config", nargs="?", help="path to JSON config")
    ap.add_argument("-o", "--out", help="output PPTX path")
    ap.add_argument("--example", action="store_true",
                    help="write example config and PPTX in CWD")
    args = ap.parse_args()

    if args.example or not args.config:
        with open("gantt_example.json", "w", encoding="utf-8") as f:
            json.dump(EXAMPLE, f, indent=2, ensure_ascii=False)
        out = args.out or "Gantt_Editorial_Example.pptx"
        build(EXAMPLE, out)
        print("wrote gantt_example.json and", out)
        return

    with open(args.config, encoding="utf-8") as f:
        cfg = json.load(f)
    out = args.out or os.path.splitext(args.config)[0] + ".pptx"
    build(cfg, out)
    print("wrote", out)


if __name__ == "__main__":
    main()
