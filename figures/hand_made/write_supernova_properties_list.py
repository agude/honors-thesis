from math import sqrt,log10

def returndicts(file,sig1,sig2,sig3,sig4,sig5):
    c = 299792.458 # km/s
    alpha = -2.08404837532
    beta = 3.61019520579
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
	    cz = float(line[1])
	    z  = cz / c
	    M = hubble(float(line[1]))
	    mag  = float(line[2])
	    magerr = float(line[3])
	    color = float(line[4])
	    colorerr = float(line[5])
	    stretch  = float(line[6])
	    sg1 = sig1[sn]
	    sg2 = sig2[sn]
	    sg3 = sig3[sn]
	    sg4 = sig4[sn]
	    sg5 = sig5[sn]
	    strcor = ( mag - M - alpha*(stretch -1) )
	    colcor = ( mag - M - beta*color )
	    sccor = ( mag - M - alpha*(stretch -1) - beta*color)

	    print '%s %s %0.5f %s %0.5f %0.5f %0.5f %0.5f %0.5f %0.5f %0.5f %0.5f %0.5f %0.5f %0.5f %0.5f %0.5f'%(sn,'z',z,'MJD',color,colorerr,stretch,mag,strcor,colcor,sccor,magerr,sg1,sg2,sg3,sg4,sg5)

def readin(file):
    sig1 = {}
    sig2 = {}
    sig3 = {}
    sig4 = {}
    sig5 = {}
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
	    sig1[sn] = float(line[12])
	    sig2[sn] = float(line[13])
	    sig3[sn] = float(line[14])
	    sig4[sn] = float(line[15])
	    sig5[sn] = float(line[16])

    return (sig1,sig2,sig3,sig4,sig5)

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

########
readinf = 'supernova_properties_list.dat'

(sig1,sig2,sig3,sig4,sig5) = readin(readinf)
returndicts('hubble.dat',sig1,sig2,sig3,sig4,sig5)
