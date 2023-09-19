def safe_input( prompt ):
    try:
        line = input( prompt )
        return( line, True )
    except EOFError:
        return( "", False )

cFlag = True
while cFlag:
    words,cFlag = safe_input("")
    for w in words.split():
        print(w)
