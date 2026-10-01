# editorial-deck

An [Agent Skill](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills)
that produces **Elegant-Editorial** PowerPoint decks and charts: warm paper
background, Georgia serif type, antique-gold brackets and rules, dotted grids,
and muted low-saturation flat fills. It is built for research proposals (e.g.
GRF), academic reports, work plans and timelines.

Works with **Claude Code** and any agent that loads the standard
`SKILL.md` skill format. Output is an editable 16:9 `.pptx`.

## What it gives you

- `scripts/build_gantt.py` — a parameterised Gantt/timeline generator. Give it
  a JSON config (title, time ticks, year/phase bands, tasks) and it renders a
  consistent editorial timeline.
- `scripts/deck_lib.py` — design tokens plus shape/text primitives, so colours,
  type and the signature gold brackets / dotted grids never drift.
- `references/design-system.md` — full colour, typography and layout spec.
- `references/slide-patterns.md` — cover, divider, content, figure, pull-quote
  and closing layouts for a complete deck.
- `assets/gantt_example.json` — sample Gantt config matching the reference chart.

## Install

Requires Python 3 and `python-pptx`:

```bash
pip install python-pptx
```

Then place this folder in one of your skill directories.

**Claude Code — all projects (user level):**

```bash
# macOS / Linux
git clone https://github.com/organocatalysis-dot/editorial-deck.git ~/.claude/skills/editorial-deck
```
```powershell
# Windows
git clone https://github.com/organocatalysis-dot/editorial-deck.git "$env:USERPROFILE\.claude\skills\editorial-deck"
```

**Claude Code — single project only:**

```bash
git clone https://github.com/organocatalysis-dot/editorial-deck.git .claude/skills/editorial-deck
```

Restart Claude Code (and trust the project folder if prompted).

## Use

Ask in natural language, for example:

- "Build an editorial-style Gantt chart for these work packages and dates."
- "Make a work-plan timeline with the warm paper serif look."
- "Create a full proposal deck in the editorial style."

To generate a Gantt chart directly:

```bash
python scripts/build_gantt.py config.json -o timeline.pptx
```

Run with no arguments (or `--example`) to write a sample config and PPTX.

### Config schema

```json
{
  "title": "Work Plan & Timeline",
  "subtitle": "A thirty-five-month research programme ...",
  "footer_left": "Duration shown in months; ...",
  "footer_right": "January 2028 - December 2030",
  "ticks": [{"index": 0, "label": "01/2028"}],
  "bands": [{"start": 0, "end": 12, "label": "2028"}],
  "tasks": [
    {"id": "WP1", "name": "First line of\nsecond line",
     "start": 0, "end": 24, "duration": "24 mo"}
  ]
}
```

`index` is a shared numeric coordinate: a task bar spans `start`→`end`, and a
band bracket groups an index span. See `assets/gantt_example.json`.

## Design principles

Flat muted fills; Georgia throughout; gold rules and brackets; dotted rather
than boxed grids; left-aligned titles; generous whitespace; white text only on
fills. No neon, gradients, shadows on data, pill bars or emoji. Full details in
[`references/design-system.md`](references/design-system.md).

## License

[MIT](LICENSE)
