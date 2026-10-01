# Elegant Editorial — Design System

A quiet, paper-and-ink "academic editorial" style: warm paper, serif type,
antique-gold rules, dotted grids, muted low-saturation colour. Optimised for
research proposals, reports, work plans and timelines. It should read like a
typeset journal section, never like a SaaS dashboard or a default template.

## 1. Colour

All values are sRGB hex. Use them verbatim; do not brighten or saturate.

| Role | Hex | Use |
|---|---|---|
| Paper | `FAF8F3` | slide background (warm off-white) |
| Ink | `2C2A24` | headings, primary body |
| Sub | `6E675C` | secondary text, labels, captions |
| Gold | `A98B4E` | brackets, short rules, accents |
| Moss | `33574B` | emphasis labels (e.g. year marks) |
| Hairline | `D8D0C0` | thin solid dividers |
| Dot rule | `CFC7B6` | dotted horizontal rules |
| Dot column | `E3DCCB` | dotted vertical rules |

Series palette (cycled for bars / categories, in this order):

1. Slate blue `42607A`
2. Sage green `5F7E6C`
3. Clay `A67C52`
4. Dusty rose `8E5B52`
5. Muted violet `7A6E8A`
6. Antique brass `B08D3E`
7. Deep teal `4E7A78`
8. Terracotta `9C6B4E`

Rules:
- Prefer a single series palette for an entire chart/deck; never mix the
  palette with primary/neon colours.
- Text on a filled bar is always white. Text on paper is Ink or Sub.
- Keep fills flat (no gradients, no bevels, no drop shadows on bars).

## 2. Typography

- Serif face: **Georgia** (headings, labels, chart text, captions).
- Sans face: **Arial**, only for dense data, URLs or when a label must sit in a
  pre-existing sans document; default to Georgia.
- Numerals in charts/labels use Georgia; italic Georgia is used for durations,
  date ranges and captions.

Type scale (pt, on the 13.33 × 7.5 in 16:9 canvas):

| Role | Size | Weight / style |
|---|---|---|
| Slide title | 23 | bold |
| Chart/section title | 18–21 | bold |
| Subtitle / standfirst | 10.5 | italic |
| Band / year label | 10.5 | bold |
| Body / task name | 9.8 | regular |
| Tick / axis label | 9.4 | regular |
| Small label / id | 9 | bold |
| Bar duration | 8.8 | italic |
| Caption / footer | 8.8–9.2 | italic |

- Use loose letter-spacing for short uppercase-ish labels such as year marks
  (render as `2 0 2 8`, or `spc` in the helper).
- Line pitch for wrapped names ≈ 0.028 of slide height; never let wrapped text
  touch the row rule.

## 3. Layout and whitespace

- Outer margin ≈ 0.045–0.055 of width; keep the left edge of every text block
  aligned to one vertical axis.
- Title block sits top-left; never centre the title on editorial content
  slides.
- Reserve a label column on the left (≈ 0.25–0.28 of width); the figure area
  runs from ≈ 0.30 to ≈ 0.96.
- Generous whitespace is the main luxury cue: if a slide feels crowded, remove
  an element rather than shrinking type below the scale.
- Align tick labels to their grid positions; the first/last label may be
  centre-aligned on the boundary.

## 4. Decorative language (the identifying details)

- **Gold short rule** under the title: ≈ 0.12 of width, 0.0022 high, Gold;
  optionally continued to the right margin by a Hairline-weight rule.
- **Band brackets**: a horizontal Gold rule spanning a group, with short
  upward end ticks; the group label sits centred above it.
- **Dotted rules**: dot-dashed horizontal row separators and faint dotted
  vertical columns — never solid chart boxing.
- **End ticks**: a short vertical cap marks the end of a bar, extending just
  above and below the bar.
- Bars use a small corner radius (near-square), not pill shapes.

## 5. Do / Don't

Do: flat muted fills; Georgia; gold rules and brackets; dotted grids;
left-aligned titles; lots of paper; white text only on fills.

Don't: neon/primary colours; gradients or shadows on data; rounded pill bars;
centred titles; boxed chart frames; emoji; 3-D; heavy borders; mixing serif
and sans arbitrarily.
