import os,os.path

basedir = '/autofs/hstdata/users/agude/svn/scp/thesis/gude/figures/'
cordir = basedir+'corrections/'
specdir = basedir+'spectrabeforeafter/'
hsiaodir = basedir+'hsiao/'
ltcvdir = basedir+'ltcv/'

basestr = './figures/'
corstr = basestr+'corrections/'
specstr = basestr+'spectrabeforeafter/'
hsiaostr = basestr+'hsiao/'
ltcvstr = basestr+'ltcv/'

sns = [file.split('_')[0] for file in os.listdir(cordir) if (file.startswith('SN') and file.endswith('_correction.ps') ) ]
sns.sort()

for sn in sns:
    specfile = None
    corfile = None
    hsiaofile = None
    ltcvfile = None
    for file in os.listdir(specdir):
	if file.split('_')[0] == sn:
	    specfile = specstr+file
    for file in os.listdir(cordir):
	if file.split('_')[0] == sn:
	    corfile = corstr+file
    for file in os.listdir(ltcvdir):
	if file.split('_')[0] == sn:
	    ltcvfile = ltcvstr+file
    for file in os.listdir(hsiaodir):
	if file.split('_')[0] == sn:
	    hsiaofile = hsiaostr+file

    if specfile != None and corfile != None and hsiaofile != None and ltcvfile != None:
	print '\\begin{figure}[p]\n\centering\n\includegraphics[angle=-90,width=0.8\\textwidth]{'+str(specfile)+'}\n\hfill\n\includegraphics[angle=-90,width=0.8\\textwidth]{'+str(corfile)+'}\n\hfill\n\caption{'+str(sn)+' spectrum before and after warping, as well as the correction function used to warp.}\n\label{fig:'+str(sn)+'four1}\n\end{figure}\n'
	print '\clearpage\n'
	print '\\begin{figure}[p]\n\centering\n\includegraphics[angle=-90,width=0.8\\textwidth]{'+str(ltcvfile)+'}\n\hfill\n\includegraphics[angle=-90,width=0.8\\textwidth]{'+str(hsiaofile)+'}\n\hfill\n\caption{'+str(sn)+' lightcurve fit, as well as the best fit for Hsiao template warped using the Cardelli law to match the spectrum.}\n\label{fig:'+str(sn)+'four2}\n\end{figure}\n'
	print '\clearpage\n'
