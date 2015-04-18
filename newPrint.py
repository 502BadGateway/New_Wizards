import re
from os import listdir
from os.path import isfile, join
onlyfiles = [ f for f in listdir(".") if isfile(join(".",f)) ]

for files in onlyfiles:
    f = open(files, "r" )
    newsrc = re.sub( "print \"(.*?)\"", "print( \"\\1\" )", f.read() )
    f.close()

    f = open( files, "w" )
    f.write( newsrc )
    f.close()
