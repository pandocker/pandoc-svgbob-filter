# pandoc-svgbob-filter
Pandoc filter to render svgbob

# Requirements

This filter requires `svgbob` and `rsvg-convert` in `$PATH`

# Install

install by pip-git:

`$ pip3 install git+https://github.com/pandocker/pandoc-svgbob-filter.git`

# Options

Reference svgbob help (`svgbob --help`)

```
svgbob 0.3.2
SvgBobRus is an ascii to svg converter

USAGE:
    svgbob [FLAGS] [OPTIONS] [input] [SUBCOMMAND]

FLAGS:
    -h, --help       Prints help information
    -s               parse an inline string
    -V, --version    Prints version information

OPTIONS:
        --font-family <font-family>      text will be rendered with this font (default: 'arial')
        --font-size <font-size>          text will be rendered with this font size (default: 14)
    -o, --output <output>                where to write svg output [default: STDOUT]
        --scale <scale>                  scale the entire svg (dimensions, font size, stroke width) by this factor
                                         (default: 1)
        --stroke-width <stroke-width>    stroke width for all lines (default: 2)

ARGS:
    <input>    svgbob text file or inline string to parse [default: STDIN]

SUBCOMMANDS:
    build    Batch convert files to svg.
    help     Prints this message or the help of the given subcommand(s)
```

Filter options inherits options for svgbob itself.
They are applied as attributes or preset by setting metadata

| Filter option  | yaml metadata         | Description                                                               | default value |
|:---------------|:----------------------|:--------------------------------------------------------------------------|:-------------:|
| `font-family`  | `svgbob.font-family`  | Text will be rendered with this font                                      |    "Arial"    |
| `font-size`    | `svgbob.size`         | text will be rendered with this font size                                 |      14       |
| `scale`        | `svgbob.scale`        | scale the entire svg (dimensions, font size, stroke width) by this factor |       1       |
| `stroke-width` | `svgbob.stroke-width` | stroke width for all lines                                                |       2       |

# Sample Markdown

```markdown
---
# YAML frontmatter
svgbob:
  font-family: "Source Code Pro"
#  font-size: 12
#  scale: 2
#  stroke-width: 3
...

[Example](data/svgbob.bob){.svgbob font-size=14 stroke-width=2 scale=3}
```

[Example](data/svgbob.bob){.svgbob font-size=14 stroke-width=2 scale=3}

# Usage example

```bash
pandoc README.md -F pandoc-svgbob-filter -o README.html
```
