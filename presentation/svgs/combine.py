from os.path import isfile
from os import listdir
from sys import argv
from commands import getoutput

image = argv[1]
ang = argv[2]

files = [svg for svg in listdir('.') if ( svg.endswith('.svg') and ( image in svg ) ) ]

file98bp = None
png98bp = None
file98eg = None
png98eg = None
file99ac = None
png99ac = None
file00dk = None
png00dk = None

if len(files) != 4:
    raise "More or less than four files!"

for file in files:
    print file
    if '98bp' in file:
        print 'Found 98bp'
        file98bp = file
        png98bp = (file.split('.svg')[0])+'.png'
    elif '98eg' in file:
        print 'Found 98eg'
        file98eg = file
        png98eg = (file.split('.svg')[0])+'.png'
    elif '99ac' in file:
        print 'Found 99ac'
        file99ac = file
        png99ac = (file.split('.svg')[0])+'.png'
    elif '00dk' in file:
        print 'Found 00dk'
        file00dk = file
        png00dk = (file.split('.svg')[0])+'.png'

if file98bp == None or file98eg == None or file99ac == None or file00dk == None:
    raise "Could not ID all SNs."

print "Converting to pngs"
getoutput('convert %s -rotate %i %s'%(file98bp,int(ang),png98bp))
getoutput('convert %s -rotate %i %s'%(file98eg,int(ang),png98eg))
getoutput('convert %s -rotate %i %s'%(file99ac,int(ang),png99ac))
getoutput('convert %s -rotate %i %s'%(file00dk,int(ang),png00dk))

print "Combining"
getoutput('convert %s %s +append 1.png'%(png98bp,png98eg))
getoutput('convert %s %s +append 2.png'%(png99ac,png00dk))
getoutput('convert 1.png 2.png -append 3.png')
