theCount = 0
# TargetWords = [ "the", "The" ]
TargetWords = ['outside', 'today', 'weather', 'raining', 'nice', 'rain',
'snow', 'day', 'winter', 'cold' ]
word = input("Word: ")
if word in TargetWords:
     theCount = theCount + 1

# if word == 'the':
#     theCount = theCount + 1
# elif word == 'The':
#     theCount = theCount + 1
print( "Total count %s" % (theCount) )
