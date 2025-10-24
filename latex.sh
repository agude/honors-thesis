#!/bin/sh

latex ms
bibtex ms
latex ms
latex ms
dvips -o ms.ps ms.dvi
rm -f ms.aux
rm -f ms.blg
#rm -f ms.bbl
rm -f ms.log
rm -f ms.dvi
