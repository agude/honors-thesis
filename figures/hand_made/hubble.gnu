# Everyone uses these commands
set terminal postscript enhanced color solid landscape "Helvetica" 14
set xlabel 'cz'
set ylabel 'B Band Max Mag.'
set yrange [11:18]
set key right bottom
h(x) = -19.31+5*log10( x / 71.9 ) + 25

# No correction
set title  'Hubble Diagram'
set output '01_hubble.ps'
p h(x) lt 3 lw 1 t 'Hubble Law H_{0} = 71.9', 'hubble.dat' u 2:3:4 w err lt 1 t 'Supernovae'

# No correction
set title  'Hubble Diagram'
set output '02_hubble_stretch_corrected.ps'
p h(x) lt 3 lw 1 t 'Hubble Law H_{0} = 71.9', 'hubble.dat' u 2:($3+1.24*($7-1)):4 w err lt 1 t 'Supernovae with Stretch Correction'

# No correction
set title  'Hubble Diagram'
set output '03_hubble_color_corrected.ps'
p h(x) lt 3 lw 1 t 'Hubble Law H_{0} = 71.9', 'hubble.dat' u 2:($3-2.28*$5):4 w err lt 1 t 'Supernovae with Color Correction'

# No correction
set title  'Hubble Diagram'
set output '04_hubble_color_stretch_corrected.ps'
p h(x) lt 3 lw 1 t 'Hubble Law H_{0} = 71.9', 'hubble.dat' u 2:($3+1.24*($7-1)-2.28*$5):4 w err lt 1 t 'Supernovae with Stretch and Color Correction'

# No correction
set title  'Hubble Diagram'
set output '08_hubble_color_stretch_sig_corrected.ps'
p h(x) lt 3 lw 1 t 'Hubble Law H_{0} = 71.9', 's_c_sig1_dispersion.dat' w err lt 1 t 'Supernovae with Stretch, Color, and First Normalized Weight Correction'

# No correction
set title  'Hubble Diagram'
set output '07_hubble_sig_corrected.ps'
p h(x) lt 3 lw 1 t 'Hubble Law H_{0} = 71.9', 'disp_sig1.dat' w err lt 1 t 'Supernovae with First Normalized Weight Correction'

# Next two use these options
set auto
set key right top

# No correction
set title  'Fitting for beta'
set output '05_hubble_beta.ps'
set xlabel 'Color'
set ylabel 'm - \alpha (S-1) - M'
#p 'hubble.dat' u 5:($3+1.24*($7-1) - h($2)):4 w err lt 1 t '', 2.28*x lt 3 lw 1 t 'beta = 2.28'
p 'beta_fit.dat' w points lt 1 t '', 3.61019520579*x lt 3 lw 1 t 'beta = 3.610'

# No correction
set title  'Fitting for alpha'
set output '06_hubble_alpha.ps'
set xlabel 'Stretch - 1'
set ylabel 'm - beta*c  - M'
#p 'hubble.dat' u ($7-1):($3-2.28*$5 - h($2)):4 w err lt 1 t '', -1.24*x lt 3 lw 1 t 'alpha = -1.24'
p 'alpha_fit.dat' w po lt 1 t '', -2.08404837532*x lt 3 lw 1 t 'alpha = -2.084'
