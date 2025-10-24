# Everyone uses these commands
set terminal postscript enhanced color solid landscape "Helvetica" 14
set xlabel 'Angstroms'
set ylabel 'Extinction Factor'
set key right bottom

# No correction
set title  'Cardelli Law Corrction'
set output 'ccm.ps'
p 'red_0.1.dat' w lines lw 2 t 'A_{V}=0.31', 'red_0.2.dat' w lines lw 2 t 'A_{V}=0.62', 'red_0.3.dat' w lines lw 2 t 'A_{V}=0.93', 'red_0.4.dat' w lines lw 2 t 'A_{V}=1.24', 'red_0.5.dat' w lines lw 2 t 'A_{V}=1.55'
