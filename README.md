# sheetmill

`sheetmill` installs the sheetmill packages, a set of pure-Python tools for working with Excel
files. It contains no code of its own; each package is imported under its own name.

```bash
pip install sheetmill
```

Today that installs one package:

- [xlformat](https://github.com/sheetmill/xlformat): applies Excel number formats to values and
  returns the text Excel displays ([PyPI](https://pypi.org/project/xlformat/),
  [documentation](https://xlformat.readthedocs.io)).

Two more will be added as they are released:

- [sheetpeek](https://github.com/sheetmill/sheetpeek): renders workbooks to HTML, Markdown and
  terminal output.
- [xlformula](https://github.com/sheetmill/xlformula): evaluates Excel formulas.

Each package also installs and works on its own.

## License

MIT.
