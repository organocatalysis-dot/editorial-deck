---
name: editorial-deck
description: >-
  Generate Elegant-Editorial style PowerPoint decks and charts: warm paper
  background, Georgia serif type, antique-gold brackets and rules, dotted
  grids, muted low-saturation (slate/sage/clay/rose) flat fills. Use for
  research proposals (e.g. GRF), academic reports, work plans, timelines and
  Gantt charts, or whenever the user asks for an "elegant editorial",
  "paper-and-ink", "serif", "warm", "academic journal" look, or asks to reuse
  the approved editorial Gantt/timeline style. Produces editable 16:9 PPTX.
---

# Editorial Deck

Build quiet, typeset "academic editorial" PPTX — never default templates or
dashboard styling. Two paths: a parameterised Gantt generator, and a manual
path for full decks.

Requirements: Python 3 with `python-pptx` (`pip install python-pptx`). The
scripts are platform-independent; Georgia is a system font on both macOS and
Windows.

## Step 1 — Choose the path

- **Gantt / timeline / work-plan chart** → use `scripts/build_gantt.py`
  (deterministic; do not redraw by hand).
- **Full deck or other slide types** (cover, content, quote, closing) → read
  `references/slide-patterns.md` and build with `scripts/deck_lib.py`.

In both cases follow `references/design-system.md` for colour, type scale and
the identifying decorative details. Read it before designing any slide.

## Step 2A — Gantt chart

1. Extract from the user: title, subtitle, time ticks, year/phase bands, and
   tasks (id, name, start, end, duration). Use the user's data verbatim; do
   not invent dates.
2. Write a config JSON (schema in the script header; start from
   `assets/gantt_example.json`). `index` is a shared numeric coordinate; a
   task bar spans start→end and a band bracket groups an index span.
3. Generate:
   ```bash
   python3 scripts/build_gantt.py config.json -o timeline.pptx
   ```
   With no config, `--example` writes `assets/gantt_example.json`-style sample
   output for reference.
4. Render and inspect (see Step 3). Fix data/layout in the config and rerun;
   do not alter the generated chart by hand.

## Step 2B — Full deck

1. Read `references/slide-patterns.md`; pick a pattern per slide.
2. Build shapes only via `scripts/deck_lib.py` helpers (tokens, anchored text,
   brackets, dotted rules). Keep one left axis and one type scale throughout.
3. Assemble slides in order; set every background to Paper and disable
   inherited shape shadows.

## Step 3 — Verify before delivery

- Render the PPTX and inspect every slide:
  - macOS: Quick Look `qlmanage -t -s 2000 -o <dir> <file>.pptx`, or open in
    Keynote / PowerPoint.
  - Windows: open in PowerPoint (qlmanage is unavailable).
- Check: titles on one line and left-aligned; tick labels on their grid
  positions; bar text (id / duration) not clipped or overlapping end ticks;
  no neon, gradients, shadows on data, pill bars or emoji.
- Confirm all user dates/numbers are preserved, then deliver the PPTX.

## Resources

- `scripts/deck_lib.py` — design tokens + shape/text primitives (import, do
  not duplicate).
- `scripts/build_gantt.py` — parameterised editorial Gantt generator.
- `references/design-system.md` — full colour, typography, layout and
  do/don't specification.
- `references/slide-patterns.md` — cover/divider/content/figure/quote/closing
  layouts.
- `assets/gantt_example.json` — sample Gantt config matching the approved chart.
