#Makefile to produce Dipole paper

input:=$(shell ls ./input/*.tex)
pyfigures:=$(shell ls ./figures/*.py)
figures=$(pyfigures:%.py=%.pdf)

all: $(figures) $(input) Dipole.pdf 

Dipole.pdf: Dipole.tex thebib.bib $(input) 
	pdflatex -draftmode Dipole
	bibtex Dipole
	pdflatex -draftmode Dipole
	pdflatex Dipole

%.pdf: %.py 
	python $<

clean: 
	rm *.bbl *.blg *.log *.aux *.dvi ./figures/*.pdf *~ ./figures/*~ ./input/*~

