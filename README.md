# pandoc-svgbob-filter
Pandoc filter to render svgbob

# Requirements

This filter requires `svgbob` and `rsvg-convert` in `$PATH`

# Install

install by pip-git:

`$ pip3 install git+https://github.com/pandocker/pandoc-svgbob-filter.git`

# Samples

```markdown
[Example](bob.bob){.svgbob font-family="Source Code Pro" font-size=14 stroke-width=2 scale=3}
```

[Example](bob.bob){.svgbob}

# Options

| Option         | Description                                                               | default value |
|:---------------|:--------------------------------------------------------------------------|:-------------:|
| `font-family`  | Text will be rendered with this font                                      |    "Arial"    |
| `font-size`    | text will be rendered with this font size                                 |      14       |
| `scale`        | scale the entire svg (dimensions, font size, stroke width) by this factor |       1       |
| `stroke-width` | stroke width for all lines                                                |       2       |

# Usage example

```bash
pandoc README.md -F pandoc-svgbob-filter -o README.html
```
