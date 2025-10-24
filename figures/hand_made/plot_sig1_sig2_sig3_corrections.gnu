set terminal postscript enhanced color solid landscape "Helvetica" 14
h(x) = -19.31+5*log10( x / 71.9 ) + 25


# Sigma 1
set output 'sig1.ps'
set xlabel 'First Normalized Weight'
set ylabel 'm - M'
set title  'First Normalized Weight'
p 'sig1.dat' lt 1 w err t 'Supernova', 0.826302610626-0.720480080499*x t 'Weighted Least Squares Fit' lw 2 lt 3

# Sigma 2
set output 'sig2.ps'
set xlabel 'Second Normalized Weight'
set ylabel 'm - M - A*sig1'
set title  'Second Normalized Weight'
p 'sig2.dat' lt 1 w err t 'Supernova', -0.0885640315008+0.37612138586*x t 'Weighted Least Squares Fit' lw 2 lt 3

# Sigma 3
set output 'sig3.ps'
set xlabel 'Third Normalized Weight'
set ylabel 'm - M - A*sig1 - B*sig2'
set title  'Third Normalized Weight'
p 'sig3.dat' lt 1 w err t 'Supernova', -0.0885640315008+0.464685417361*x t 'Weighted Least Squares Fit' lw 2 lt 3

# Sigma 4
set output 'sig4.ps'
set xlabel 'Forth Normalized Weight'
set ylabel 'm - M - A*sig1 - B*sig2 - C*sig3'
set title  'Forth Normalized Weight'
p 'sig4.dat' lt 1 w err t 'Supernova', -0.0118552311549+0.204263918675*x t 'Weighted Least Squares Fit' lw 2 lt 3

# Sigma 5
set output 'sig5.ps'
set xlabel 'Fifth Normalized Weight'
set ylabel 'm - M - A*sig1 - B*sig2 - C*sig3 - D*sig4'
set title  'Fifth Normalized Weight'
p 'sig5.dat' lt 1 w err t 'Supernova', 0.0611255824323+0.548840622996*x t 'Weighted Least Squares Fit' lw 2 lt 3
