theCount = 0
while True:
    try:
        word = input("Word: ")
    except EOFError:
        break
    if word == 'the':
        theCount = theCount + 1
    elif word == 'The':
        theCount = theCount + 1
    print( "Total count %s" % (theCount) )
