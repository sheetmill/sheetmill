"""Installs the sheetmill packages; each is imported under its own name.

Installing ``sheetmill`` installs:

- ``xlformat``: applies Excel number formats to values and returns the text Excel displays
  (https://pypi.org/project/xlformat/, https://xlformat.readthedocs.io).
- ``sheetpeek``: renders workbooks as HTML, Markdown and terminal text
  (https://pypi.org/project/sheetpeek/, https://sheetpeek.readthedocs.io).

``pip install "sheetmill[rich]"`` also installs ``rich`` for sheetpeek's styled terminal
output. A formula engine, in development, will be added when it is released. This package
contains no code of its own.
"""

__version__ = "0.2.0"
