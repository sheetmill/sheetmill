# sheetmill

`sheetmill` installs the sheetmill packages, a set of pure-Python tools for working with Excel
files. It contains no code of its own; each package is imported under its own name.

```bash
pip install sheetmill
```

That installs three packages:

- [xlformat](https://github.com/sheetmill/xlformat): applies Excel number formats to values and
  returns the text Excel displays ([PyPI](https://pypi.org/project/xlformat/),
  [documentation](https://xlformat.readthedocs.io)).
- [sheetpeek](https://github.com/sheetmill/sheetpeek): renders workbooks as HTML, Markdown and
  terminal text, showing what Excel shows ([PyPI](https://pypi.org/project/sheetpeek/),
  [documentation](https://sheetpeek.readthedocs.io)).
- [xlrecalc](https://github.com/sheetmill/xlrecalc): recalculates Excel workbooks in pure Python
  and writes the results back as cached values ([PyPI](https://pypi.org/project/xlrecalc/),
  [documentation](https://xlrecalc.readthedocs.io)).

For sheetpeek's styled terminal output, which uses [rich](https://pypi.org/project/rich/),
install the `rich` extra:

```bash
pip install "sheetmill[rich]"
```

Each package also installs and works on its own.

## License

MIT.
