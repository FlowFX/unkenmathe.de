# Unkenmathe.de

![Project Status](https://img.shields.io/badge/status-alpha-yellow.svg)
[![Build Status](https://travis-ci.org/FlowFX/unkenmathe.de.svg?branch=master)](https://travis-ci.org/FlowFX/unkenmathe.de)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![codecov](https://codecov.io/gh/FlowFX/unkenmathe.de/branch/master/graph/badge.svg)](https://codecov.io/gh/FlowFX/unkenmathe.de)
[![Waffle.io - Issues in progress](https://badge.waffle.io/FlowFX/unkenmathe.de.png?label=in%20progress&title=In%20Progress)](http://waffle.io/FlowFX/unkenmathe.de)

The goal of [unkenmathe.de](https://www.unkenmathe.de/) is to provide a resource of exercises and exercise sheets for German mathematics teachers. Using their own or community-provided exercises, written in Markdown and LaTeX, they can create beautiful exercise sheets. Eventually.

All exercises and sheets are distributed under a [Creative Commons License](https://creativecommons.org/) that allows easy and legal distribution and re-use. Something that German law and school material publishers do not offer.

## Examples
### Preview exercise as PDF
![Preview exercise as PDF](doc/um_preview_exercise_pdf.gif)

### Edit exercise
![Preview exercise as PDF](doc/um_edit_exercise.gif)

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
