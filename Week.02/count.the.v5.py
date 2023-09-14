# Next feature:
#	Put input into a def safe_input()
def safe_input( prompt ):
    try:
        word = input( prompt )
        return( word )
    except EOFError:
        return( "<STOP>" )

theCount = 0
while True:
    word = safe_input( "Word: " )
    if word == 'the':
        theCount = theCount + 1
    elif word == 'The':
        theCount = theCount + 1
    elif word == '<STOP>':
        break
    print( "Count count %s" % (theCount) )

print( "Total count %s" % (theCount) )
