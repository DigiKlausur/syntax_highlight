# syntax_highlight
Cell magic to highlight different languages

## Installation

```
pip install --no-cache-dir git+https://github.com/Digiklausur/syntax_highlight
jupyter nbextension install --py --sys-prefix syntax_highlight
jupyter nbextension enable --py --sys-prefix syntax_highlight
```

## Usage

First import it:

`import syntax_highlight`

Then use it in a cell:

`%%syntax java`

## Modes

Supported languages are `c`, `java`, `sql`.
