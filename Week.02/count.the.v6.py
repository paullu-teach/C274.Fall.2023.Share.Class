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
    word, cFlag = safe_input( "Word: " )
    if word == 'the':
        theCount = theCount + 1
    elif word == 'The':
        theCount = theCount + 1
    print( "Count count %s" % (theCount) )
    if cFlag == True:
        lastWord = word

print( "Total count %d.  Last word:  %s" % (theCount, lastWord) )
