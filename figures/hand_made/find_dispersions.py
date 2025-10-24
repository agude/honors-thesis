from math import sqrt,log10

def returndicts(file):
    c = 299792.458 # km/s
    sns  = []
    sig1 = {}
    sig2 = {}
    sig3 = {}
    sig4 = {}
    sig5 = {}
    cz   = {}
    M    = {}
    mag  = {}
    magcc  = {}
    magsc  = {}
    magscc  = {}
    magerr = {}
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
	    sig1[sn] = float(line[12])
	    sig2[sn] = float(line[13])
	    sig3[sn] = float(line[14])
	    sig4[sn] = float(line[15])
	    sig5[sn] = float(line[16])
	    cz[sn] = float(line[2])*c
	    M[sn] = hubble(float(line[2])*c)
	    mag[sn]  = float(line[7])
	    magcc[sn]  = float(line[8])
	    magsc[sn]  = float(line[9])
	    magscc[sn]  = float(line[10])
	    magerr[sn] = float(line[11])

    sns.sort()

    return (sns,sig1,sig2,sig3,sig4,sig5,cz,M,mag,magcc,magsc,magscc,magerr)

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

def disspersion(data):
    xs = [x for x in data]
    xs.sort()
    ys = [data[x] for x in xs]

    N = float(len(ys))
    average = sum(ys) / N

    difs = [ ( y - average )**2 for y in ys]
    std = sqrt( ( 1 / ( N + 1 ) ) * sum( difs ) )

    return (average,std)

def disspersion2sig(data,std):
    xs = [x for x in data]
    xs.sort()
    ys = []
    rejected = {}
    for x in xs:
	if abs(data[x]) < 2*std:
	    ys.append(data[x])
	    rejected[x] = ''
	else:
	    rejected[x] = r'$^{*}$'
	    continue
	
    N = float(len(ys))
    print N
    average = sum(ys) / N

    difs = [ ( y - average )**2 for y in ys ]
    std = sqrt( ( 1 / ( N + 1 ) ) * sum( difs ) )

    return (average,std,rejected)

##############################
file = 'supernova_properties_list.dat'
c = 299792.458 # km/s
##############################

(sns,sig1,sig2,sig3,sig4,sig5,cz,Model,mag,magcc,magsc,magscc,magerr) = returndicts(file)

uncor = {}
color = {}
stretch = {}
colstr  = {}
sigma1 = {}
sigma2 = {}
sigma3 = {}
sig1sig2 = {}
david = {}
for sn in sns:
    m = mag[sn]
    cc = magcc[sn]
    sc = magsc[sn]
    scc = magscc[sn]
    s1 = sig1[sn]
    s2 = sig2[sn]
    s3 = sig3[sn]
    s4 = sig4[sn]
    s5 = sig5[sn]
    cv = cz[sn]
    M  = Model[sn]
    merr = magerr[sn]

    uncor[sn] = ( m - M)
    color[sn] = ( cc )
    stretch[sn] = ( sc )
    colstr[sn] = ( scc )
    #sigma1[sn] = ( m - s1*(-0.720480080499) -0.826302610626 - M)
    sigma1[sn] = ( m - s1*(-0.711481079904) -0.742768690895 - M)
    sigma2[sn] = ( m - s1*(-0.711481079904) -0.742768690895 - s2*0.402474744303 - 0.702501739747- M)
    sigma3[sn] = ( m - s1*(-0.711481079904) -0.742768690895 - s2*0.402474744303 - 0.702501739747 - s3*(-0.300026995444)-0.300026995444 - M )
#    sig1sig2[sn] = ( m - s3*0.464685417361 - s1*(-0.720480080499) - M)
    #david[sn]    = (scc - s1*(-0.0121213581099)-0.291972470836 -M )#-s2*(0.0586716508906)-0.124885049762 -s3*(-0.0662133988709)-0.0662133988709 -s4*(-0.122159213014)-0.0950208586408 -s5*(0.0825893208611) -0.293069482738- M)
    david[sn]    = (scc - s1*(0.455025167024)-(-0.140875271646) )#-s2*(0.0586716508906)-0.124885049762 -s3*(-0.0662133988709)-0.0662133988709 -s4*(-0.122159213014)-0.0950208586408 -s5*(0.0825893208611) -0.293069482738- M)

(uncorA,uncorSTD) = disspersion(uncor)
(colorA,colorSTD) = disspersion(color)
(stretchA,stretchSTD) =  disspersion(stretch)
(colstrA,colstrSTD) = disspersion(colstr)
(sigma1A,sigma1STD) =  disspersion(sigma1)
(sigma2A,sigma2STD) = disspersion(sigma2)
(sigma3A,sigma3STD) = disspersion(sigma3)
#(sig1sig2A,sig1sig2STD) = disspersion(sig1sig2)
(davidA,davidSTD) = disspersion(david)

(uncorA2,uncorSTD2,uncorr) = disspersion2sig(uncor,uncorSTD)
(colorA2,colorSTD2,colorr) = disspersion2sig(color,colorSTD)
(stretchA2,stretchSTD2,stretchr) = disspersion2sig(stretch,stretchSTD)
(colstrA2,colstrSTD2,colstrr) = disspersion2sig(colstr,colstrSTD)
(sigma1A2,sigma1STD2,sigma1r) = disspersion2sig(sigma1,sigma1STD)
(sigma2A2,sigma2STD2,sigma2r) = disspersion2sig(sigma2,sigma2STD)
(sigma3A2,sigma3STD2,sigma3r) = disspersion2sig(sigma3,sigma3STD)
#(sig1sig2A2,sig1sig2STD2) =  disspersion2sig(sig1sig2,sig1sig2A,sig1sig2STD)
(davidA2,davidSTD2,davidr) = disspersion2sig(david,davidSTD)

print "--------------------------------------------------------------------"
for sn in sns:
    print r'%s & %0.3f%s & %0.3f%s & %0.3f%s & %0.3f%s & %0.3f%s & %0.3f%s & %0.3f%s & %0.3f%s \\'%(sn,uncor[sn],uncorr[sn],color[sn],colorr[sn],stretch[sn],stretchr[sn],colstr[sn],colstrr[sn],sigma1[sn],sigma1r[sn],sigma2[sn],sigma2r[sn],sigma3[sn],sigma3r[sn],david[sn],davidr[sn])
print '\hline'
print r'Dispersion & %0.3f & %0.3f & %0.3f & %0.3f & %0.3f & %0.3f & %0.3f & %0.3f \\'%(uncorSTD,colorSTD,stretchSTD,colstrSTD,sigma1STD,sigma2STD,sigma3STD,davidSTD)
print r'2$\sigma$ Cut & %0.3f & %0.3f & %0.3f & %0.3f & %0.3f & %0.3f & %0.3f & %0.3f \\'%(uncorSTD2,colorSTD2,stretchSTD2,colstrSTD2,sigma1STD2,sigma2STD2,sigma3STD2,davidSTD2)
