# Security policy

## Where to report

sheetmill contains no code of its own: it installs the sheetmill packages. Report a security
problem in the repository of the package that holds the code, through that repository's private
vulnerability reporting:

- [xlformat](https://github.com/sheetmill/xlformat): Excel number formats.
- [sheetpeek](https://github.com/sheetmill/sheetpeek): rendering workbooks as HTML, Markdown and
  terminal text.
- [xlrecalc](https://github.com/sheetmill/xlrecalc): recalculating workbooks.
- [xlio](https://github.com/sheetmill/xlio): the reader sheetpeek and xlrecalc share, which comes
  in through them; it reads xlsx and CSV files, including untrusted ones.

Report here only a problem with the sheetmill package itself: its packaging or the dependency
ranges it declares.

## Reporting a vulnerability

Please report security problems privately, through GitHub's private vulnerability reporting:
open the repository's **Security** tab and choose **Report a vulnerability**
(https://github.com/sheetmill/sheetmill/security/advisories/new for sheetmill itself). Do not open
a public issue.

Useful in a report: the sheetmill version, the versions of the packages it installed
(`pip list`), and what happens.

## Supported versions

sheetmill is in alpha. Only its latest release receives fixes.

## What happens after a report

A report about sheetmill itself is acknowledged and fixed in its next release, whose changelog
states the fix in its Security section. Reporters are credited there unless they prefer not to
be. A problem in one of the packages it installs is fixed in that package, and released there.
