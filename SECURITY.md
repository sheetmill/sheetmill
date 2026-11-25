# Security policy

## Reporting a vulnerability

Please report security problems privately, through GitHub's private vulnerability reporting:
open the repository's **Security** tab and choose **Report a vulnerability**
(https://github.com/sheetmill/sheetmill/security/advisories/new). Do not open a public issue.

Useful in a report: the version, a file or steps that reproduce the problem (a crafted workbook is fine), and what
happens (a crash, a hang, memory use, output that is not escaped, a limit that does not hold).

## Supported versions

sheetmill is in alpha. Fixes go into the next release; only the latest release receives fixes. Here that is the
latest release of sheetmill itself, which contains no code of its own: a problem in a package it installs (xlformat,
sheetpeek or xlrecalc) belongs in that package's repository, reported there the same way.

## What happens after a report

The report is acknowledged, reproduced and fixed in the next release, whose changelog states the fix in its Security
section. Reporters are credited there unless they prefer not to be. If the problem also affects another sheetmill
package, that package is fixed as well.
