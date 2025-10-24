from math import sqrt,log10

def returndicts(file):
    sns  = []
    sig1 = {}
    sig2 = {}
    sig3 = {}
    sig4 = {}
    sig5 = {}
    cmbz = {}
    mag  = {}
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
	    cmbz[sn] = float(line[2])
	    mag[sn]  = float(line[10])
	    magerr[sn] = float(line[11])

    sns.sort()

    return (sns,sig1,sig2,sig3,sig4,sig5,cmbz,mag,magerr)

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

    return (A,Aerr,B,Berr)

def hubble(x):
    return -19.31+5*log10( x / 71.9 ) + 25

def subtracthubble(data,data2):
    finaldata = {}
    for sig1 in data:
	cv = c * data2[sig1]
	finaldata[sig1] = ( data[sig1][0] - hubble( cv ), data[sig1][1])

    return finaldata

def subtracthubbleandcor(data,data2,A,B):
    finaldata = {}
    for sig1 in data:
	cv = c * data2[sig1]
	finaldata[sig1] = ( (data[sig1][0] - hubble( cv )), data[sig1][1])

    return finaldata

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
file = 'supernova_properties_list.dat'
c = 299792.458 # km/s
##############################

(sns,sig1,sig2,sig3,sig4,sig5,cmbz,mag,magerr) = returndicts(file)

# Sig 1
sg1 = {}
for sn in sns:
    m = mag[sn]
    s1 = sig1[sn]
    cv = cmbz[sn] * c
    merr = magerr[sn]

    sg1[s1] = (m, merr)

writefile('sig1david.dat',sg1)
    
(A1,Aerr1,B1,Berr1) = weigthedlms(sg1)

print A1,Aerr1,B1,Berr1

# Sig 2
sg2 = {}
for sn in sns:
    m = mag[sn]
    s1 = sig1[sn]
    s2 = sig2[sn]
    cv = cmbz[sn] * c
    M  = hubble(cv)
    merr = magerr[sn]

    sg2[s2] = (m - A1*s1-B1, merr)

writefile('sig2david.dat',sg2)

(A2,Aerr2,B2,Berr2) = weigthedlms(sg2)
print A2,Aerr2,B2,Berr2

# Sig 3
sg3 = {}
for sn in sns:
    m = mag[sn]
    s1 = sig1[sn]
    s2 = sig2[sn]
    s3 = sig2[sn]
    cv = cmbz[sn] * c
    M  = hubble(cv)
    merr = magerr[sn]

    sg3[s3] = (m - A1*s1 - A2*s2-B1-B2, merr)

writefile('sig3david.dat',sg3)

(A3,Aerr3,B3,Berr3) = weigthedlms(sg3)
print A3,Aerr3,B3,Berr3

# Sig 4
sg4 = {}
for sn in sns:
    m = mag[sn]
    s1 = sig1[sn]
    s2 = sig2[sn]
    s3 = sig2[sn]
    s4 = sig4[sn]
    cv = cmbz[sn] * c
    M  = hubble(cv)
    merr = magerr[sn]

    sg4[s4] = (m - A1*s1 - A2*s2 - A3*s3-B1-B2-B3, merr)

writefile('sig4david.dat',sg4)

(A4,Aerr4,B4,Berr4) = weigthedlms(sg4)
print A4,Aerr4,B4,Berr4

# Sig 5
sg5 = {}
for sn in sns:
    m = mag[sn]
    s1 = sig1[sn]
    s2 = sig2[sn]
    s3 = sig2[sn]
    s4 = sig4[sn]
    s5 = sig5[sn]
    cv = cmbz[sn] * c
    M  = hubble(cv)
    merr = magerr[sn]

    sg5[s5] = (m - A1*s1 - A2*s2 - A3*s3 - A4*s4-B1-B2-B3-B4, merr)

writefile('sig5david.dat',sg5)

(A5,Aerr5,B5,Berr5) = weigthedlms(sg5)
print A5,Aerr5,B5,Berr5
