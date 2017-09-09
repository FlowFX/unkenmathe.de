# Unkenmathe.de

[![Join the chat at https://gitter.im/unkenmathe-de/Lobby](https://badges.gitter.im/unkenmathe-de/Lobby.svg)](https://gitter.im/unkenmathe-de/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

![Project Status](https://img.shields.io/badge/status-alpha-yellow.svg)
[![Build Status](https://travis-ci.org/FlowFX/unkenmathe.de.svg?branch=master)](https://travis-ci.org/FlowFX/unkenmathe.de)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![codecov](https://codecov.io/gh/FlowFX/unkenmathe.de/branch/master/graph/badge.svg)](https://codecov.io/gh/FlowFX/unkenmathe.de)

Check [unkenmathe.de](https://www.unkenmathe.de/)

## pandoc exercise.md -o exercise.tex
Using [Pandoc](http://pandoc.org/) to convert Markdown/KaTeX entries to pure LaTeX works well.

```markdown
Dies ist ein [Markdown](https://daringfireball.net/projects/markdown/)-Dokument
mit der Möglichkeit, mathematische Ausdrücke einzugeben.

## Aufgabe 2
Mathematische Ausdrücke wie $x=5$ können auch im Text stehen. Es geht aber auch komplizierter:

$$ \int_{0}^{\infty} dx\ x^2 = 99 $$
```

becomes:

```latex
Dies ist ein
\href{https://daringfireball.net/projects/markdown/}{Markdown}-Dokument
mit der Möglichkeit, mathematische Ausdrücke einzugeben.

\subsection{Aufgabe 2}\label{aufgabe-2}

Mathematische Ausdrücke wie \(x=5\) können auch im Text. Es geht aber
auch komplizierter:

\[ \int_{0}^{\infty} dx\ x^2 = 99 \]
```
