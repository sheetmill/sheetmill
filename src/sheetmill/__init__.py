"""Installs the sheetmill packages; each is imported under its own name.

Installing ``sheetmill`` installs:

- ``xlformat``: applies Excel number formats to values and returns the text Excel displays
  (https://pypi.org/project/xlformat/, https://xlformat.readthedocs.io).
- ``sheetpeek``: renders workbooks as HTML, Markdown and terminal text
  (https://pypi.org/project/sheetpeek/, https://sheetpeek.readthedocs.io).
- ``xlrecalc``: recalculates Excel workbooks in pure Python and writes the results back as
  cached values (https://pypi.org/project/xlrecalc/, https://xlrecalc.readthedocs.io).

``pip install "sheetmill[rich]"`` also installs ``rich`` for sheetpeek's styled terminal
output. This package contains no code of its own.
"""

__version__ = "0.2.0"
