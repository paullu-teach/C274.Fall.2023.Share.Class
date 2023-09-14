# Next feature:
import sys

def open_file():
    filename = "file.1w.input"
    try:
        f = open( filename, "r" )
        return( f )
    except:
        print( "File open failed: %s" % (filename) )
        sys.exit( -1 )

def safe_input( f ):
    try:
        word = f.readline().strip()
        return( word, True )
    except EOFError:
        return( "", False )

theCount = 0
cFlag = True
lastWord = ""
f = open_file()
while cFlag:
    word, cFlag = safe_input( f )
    if word == 'the' or word == 'The':
        theCount = theCount + 1
        print( "Count %d. %s" % (theCount, word) )
    else:
        print( "Skip %s" % (word) )
    if cFlag == True:
        lastWord = word

print( "Total count %d.  Last word:  %s" % (theCount, lastWord) )
