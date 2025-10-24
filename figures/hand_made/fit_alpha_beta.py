from math import sqrt,log10
#from scipy import polyfit

def returndicts(file):
    c = 299792.458 # km/s
    sns  = []
    cz   = {}
    M    = {}
    mag  = {}
    magerr = {}
    color = {}
    colorerr = {}
    stretch = {}
    try:
	f = open(file,'r')
    except IOError:
	raise "Can't open file"
    else:
	cont = f.read()
	f.close()
    
    cont = cont.splitlines()
    
    for line in cont:
	if not line.startswith('#'):
	    line = line.split()
	    sn = line[0]
	    sns.append(sn)
	    cz[sn] = float(line[1])
	    M[sn] = hubble(float(line[1]))
	    mag[sn]  = float(line[2])
	    magerr[sn] = float(line[3])
	    color[sn] = float(line[4])
	    colorerr[sn] = float(line[5])
	    stretch[sn]  = float(line[6])

	    #print sn,mag[sn]-M[sn],mag[sn],M[sn]

    sns.sort()

    return (sns,cz,M,mag,magerr,color,colorerr,stretch)

def hubble(x):
    #return -19.31+5*log10( x / 70.1 ) + 25
    return -19.31+5*log10( x / 71.9 ) + 25

def writefile(file,data):
    try:
	f = open(file,'w')
    except IOError:
	raise "Can't open write file"

    col1 = [x for x in data]
    col1.sort()
    for x in col1:
	f.write(str(x)+' '+str(data[x][0])+' '+str(data[x][1])+'\n')

    f.close()

def weigthedlms(data):
    xs = [x for x in data]
    xs.sort()
    ys = [data[x][0] for x in xs]
    ws = [1 / (data[x][1])**2 for x in xs]

    x2 = [x**2 for x in xs]
    y2 = [y**2 for y in ys]
    wx2 = [(1 / (data[x][1])**2)*x**2 for x in xs]
    wy =  [(1 / (data[x][1])**2)*data[x][0] for x in xs]
    wx =  [(1 / (data[x][1])**2)*x for x in xs]
    wxy = [(1 / (data[x][1])**2)*data[x][0]*x for x in xs]

    sumw = sum(ws)
    sumwx2 = sum(wx2)
    sumwy = sum(wy)
    sumwx = sum(wx)
    sumwxy = sum(wxy)

    delta = sumw * sumwx2 - (sumwx)**2

    A = ( sumwx2*sumwy - sumwx*sumwxy ) / delta
    B = ( sumw*sumwxy - sumwx*sumwy ) / delta

    Aerr = sqrt( sumwx2 / delta )
    Berr = sqrt( sumw / delta )

    # A + Bx
    return (A,Aerr,B,Berr)

def fitline(data):
    xs = [x for x in data]
    xs.sort()
    ys = [data[x][0] for x in xs]

    return polyfit(xs,ys,1)

def fitalpha(sns,mag,magerr,M,stretch,color,beta):
    forfit = {}
    for sn in sns:
	str = stretch[sn]
	mg = mag[sn]
	mgerr = magerr[sn]
	mod = M[sn]
	col = color[sn]

	if col > .8:
	    continue

	#forfit[str - 1.0] = ( mg - mod - beta * col - betaint, mgerr)
	forfit[str - 1.0] = ( mg - mod - beta * col, 1)

    (Aint,Aerr,Bslope,Berr) = weigthedlms(forfit)
    #(Bslope,Aint) = fitline(forfit)

    return (Bslope,Aint,forfit)

def fitbeta(sns,mag,magerr,M,stretch,color,alpha):
    forfit = {0.05 : (0.2,1)}
    for sn in sns:
	str = stretch[sn]
	mg = mag[sn]
	mgerr = magerr[sn]
	mod = M[sn]
	col = color[sn]

	if col > .8:
	    continue

	#forfit[col] = ( mg - mod - alpha * ( str - 1 ) - alphaint, mgerr)
	forfit[col] = ( mg - mod - alpha * ( str - 1 ),1)

    (Aint,Aerr,Bslope,Berr) = weigthedlms(forfit)
    #(Bslope,Aint) = fitline(forfit)

    return (Bslope,Aint,forfit)

def writefile(file,data):
    try:
        f = open(file,'w')
    except IOError:
        raise "Can't open write file"

    col1 = [x for x in data]
    col1.sort()
    for x in col1:
        f.write(str(x)+' '+str(data[x][0])+' '+str(data[x][1])+'\n')

    f.close()

##############################
file = 'hubble.dat'
c = 299792.458 # km/s
convergance = 0.001
##############################

(sns,cz,M,mag,magerr,color,colorerr,stretch) = returndicts(file)

Run = True

alpha = None
oldalpha = -1.24

"""
alphaint = None
oldalphaint = 0
"""

beta = None
oldbeta = 2.28

"""
betaint = None
oldbetaint = 0
"""

while Run:
    print "Starting new run\n\tUsing seed Alpha: %s Beta: %s"%(oldalpha,oldbeta)
    (alpha,aint,alphadat) = fitalpha(sns,mag,magerr,M,stretch,color,oldbeta)
    (beta,bint,betadat)  = fitbeta(sns,mag,magerr,M,stretch,color,alpha)

    betadiff = abs( beta - oldbeta )
    alphadiff = abs( alpha - oldalpha)

    if betadiff <= convergance and alphadiff <= convergance: 
	oldalpha = alpha
	oldbeta = beta
	writefile('alpha_fit.dat',alphadat)
	writefile('beta_fit.dat',betadat)
	Run = False
    else:
	oldalpha = alpha
	oldbeta = beta

writefile('alpha_fit.dat',alphadat)
writefile('beta_fit.dat',betadat)
print "Finished!\n\tAlpha: %s Beta: %s"%(oldalpha,oldbeta),aint,bint
