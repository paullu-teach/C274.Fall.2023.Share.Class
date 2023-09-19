theCount = 0
done = False
while not done:
    try:
        word = input("Word: ")
    except EOFError:
        done = True
        continue
    if word in [ 'exit', 'Exit' ]:
        done = True
    if word in [ 'the', 'The' ]:
        theCount = theCount + 1
print( "Total count %s" % (theCount) )

# http://pythontutor.com/visualize.html#code=theCount%20%3D%200%0Adone%20%3D%20False%0Awhile%20not%20done%3A%0A%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20word%20%3D%20input%28%22Word%3A%20%22%29%0A%20%20%20%20except%20EOFError%3A%0A%20%20%20%20%20%20%20%20done%20%3D%20True%0A%20%20%20%20%20%20%20%20continue%0A%20%20%20%20if%20word%20in%20%5B%20'exit',%20'Exit'%20%5D%3A%0A%20%20%20%20%20%20%20%20done%20%3D%20True%0A%20%20%20%20if%20word%20in%20%5B%20'the',%20'The'%20%5D%3A%0A%20%20%20%20%20%20%20%20theCount%20%3D%20theCount%20%2B%201%0Aprint%28%20%22Total%20count%20%25s%22%20%25%20%28theCount%29%20%29
