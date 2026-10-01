# Editorial Slide Patterns

Reusable page layouts for a full Elegant-Editorial deck. Coordinates are
figure fractions (x: 0 left → 1 right; y: 0 bottom → 1 top) for the 16:9
canvas, matching `scripts/deck_lib.py`. Build every shape with the library
helpers so tokens (colour, type) stay consistent.

Common anchors used below:
- Left axis `LX = 0.075`; right margin `0.94`; label column ends `0.28`;
  figure area `x 0.30–0.96`.

## 1. Cover / title page

- Eyebrow (project type / funder): `txt(LX, 0.78, size 10, SUB, italic, spc)`.
- Title: `txt(LX, 0.66, size 34–40, INK, bold, bw 0.8, bh 0.22)`; allow up to
  two lines.
- Standfirst / subtitle: `txt(LX, 0.52, size 13, SUB, italic, bw 0.7)`.
- Gold rule: `hrect(LX, 0.44, 0.14, 0.0026, GOLD)`.
- Author / affiliation / date block: bottom-left `y 0.12`, size 10.5, INK;
  secondary line SUB italic. Keep everything left-aligned; no full-page photo.

## 2. Section divider

- Large section numeral: Georgia bold 64–80, colour `E3DCCB` (faint), at
  `x LX, y 0.5`.
- Section title: `txt(LX+0.02, 0.42, size 26, INK, bold)`.
- One-line statement: `txt(LX+0.02, 0.33, size 12, SUB, italic, bw 0.6)`.
- Gold short rule above the title at `y 0.56`, width 0.10.
- Leave the right two-thirds as empty paper.

## 3. Content — bullet list

- Title: `txt(LX, 0.88, size 21, INK, bold)`; gold rule `hrect(LX, 0.83, 0.10,
  0.002, GOLD)`.
- Items start `y 0.72`, pitch `0.11`.
- Each item: a small Gold square (`hrect(LX, y+0.012, 0.012, 0.012, GOLD)`)
  followed by `txt(LX+0.035, y, size 12, INK, bw 0.8)`; an optional SUB
  sub-line at size 10 italic, 0.035 lower.
- Use 3–5 items max; no bullet glyphs, no heavy indentation.

## 4. Content — two columns

- Title as pattern 3.
- Column heads at `y 0.72`, `x 0.075` and `x 0.52`: size 12 bold MOSS, with a
  Hairline rule under each (width 0.40).
- Body lines pitch 0.055, size 10.5 INK; keep both columns the same length;
  add a faint dotted vertical divider at `x 0.49` only if needed.

## 5. Figure / chart page

- Title top-left (size 18–21 bold); figure caption below the figure, size 9
  italic SUB, prefixed "Figure N.".
- Embed charts as flat images with a Paper/transparent background; never use
  a chart style with grid boxes, shadows or default Office palettes — restyle
  to the series palette, dotted grids and Georgia labels.
- Keep the figure inside `x 0.10–0.94`, `y 0.16–0.78`; align its caption to
  the figure's left edge.
- For a Gantt chart use `scripts/build_gantt.py` rather than drawing by hand.

## 6. Pull quote / key finding

- Opening and closing quotation marks as large Georgia (size 40, GOLD).
- Quote: Georgia italic 18–22, INK, `x 0.14, y 0.5, bw 0.72`, centred as a
  block but left edge aligned.
- Attribution: size 10.5 SUB italic, below at `y 0.30`.
- Minimal page: quote, one gold rule, nothing else.

## 7. Closing / back page

- "Thank you" or project short title: Georgia bold 26 INK at `x LX, y 0.6`.
- Contact line(s): size 11 INK; email/URL may use Arial size 10.
- Gold short rule at `y 0.68`; repeat the cover's bottom-left author block for
  visual closure. No "Q&A?" clip art.

## Assembly notes

- Set the slide background to Paper for every slide.
- Insert shapes in back-to-front order; disable inherited shape shadows
  (`kill_shadow`).
- Keep one left axis and one type scale across the whole deck; variation comes
  from layout, not from new colours or fonts.
