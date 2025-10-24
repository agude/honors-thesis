set terminal postscript enhanced color solid landscape "Helvetica" 14
set style line 1 lt 1 lw 80
set output 'residual_fraction.ps'
set xrange [0.5:10.5]
set xtics 1
set yrange [0:1]
set xlabel 'Component'
set ylabel 'Residual Fraction'
set title  'Residual Fractions of Each the First Ten Components'

plot 'SN_residual_fraction.dat' u 1:4 ls 1 w imp t ''
