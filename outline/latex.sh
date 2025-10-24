#!/bin/sh

latex outline
bibtex outline
latex outline
latex outline
dvips -o outline.ps outline.dvi
rm -f outline.aux
rm -f outline.blg
rm -f outline.bbl
rm -f outline.log
rm -f outline.dvi
