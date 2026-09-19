#!/bin/bash
# Compile every fig-*.tex in this directory to a standalone PDF (and PNG if
# pdftoppm is available). Requires pdflatex with TikZ, Latin Modern, adjustbox.
set -e
cd "$(dirname "$0")"
mkdir -p out
for f in fig-*.tex; do
  n="${f%.tex}"
  {
    echo '\documentclass[border=4pt]{standalone}'
    echo '\input{preamble}'
    echo '\begin{document}'
    echo "\\input{$f}"
    echo '\end{document}'
  } > "out/$n-standalone.tex"
  (cd out && TEXINPUTS=..: pdflatex -interaction=nonstopmode -halt-on-error -output-directory . "$n-standalone.tex" >/dev/null && mv "$n-standalone.pdf" "$n.pdf" && rm -f "$n-standalone".{aux,log,tex})
  command -v pdftoppm >/dev/null && pdftoppm -r 300 -png "out/$n.pdf" "out/$n" >/dev/null
  echo "built $n"
done
