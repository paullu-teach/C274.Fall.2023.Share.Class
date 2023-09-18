catA = 0
catB = 0
catC = 0
count = 0
# nextCategory = None
# resp = [ 'A', 'A', 'A', 'B', 'B' ]
# resp = list("AAABB")
resp = list("A"*3+"B"*2)

# while nextCategory != "Q":
for nextCategory in resp:
#    nextCategory = input("Response: ")
#    count += 1
    if nextCategory == "A":
        catA = catA + 1
    elif nextCategory == "B":
        catB = catB + 1
    elif nextCategory == "C":
        catC = catC + 1
# count -= 1
count = len(resp)
print(catA, catB, catC)
print(catA/count *100, catB/count *100, catC/count *100)
