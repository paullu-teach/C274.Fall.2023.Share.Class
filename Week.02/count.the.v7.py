# Next feature:
def safe_input( prompt ):
    try:
        word = input( prompt )
        return( word, True )
    except EOFError:
        return( "", False )

theCount = 0
cFlag = True
lastWord = ""
while cFlag:
    word, cFlag = safe_input( "" )
    if word == 'the' or word == 'The':
        theCount = theCount + 1
        print( "Count %d. %s" % (theCount, word) )
    if cFlag == True:
        lastWord = word

print( "Total count %d.  Last word:  %s" % (theCount, lastWord) )
