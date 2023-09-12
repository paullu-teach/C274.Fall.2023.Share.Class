catA = 0
catB = 0
catC = 0
count = 0
nextCategory = None

while nextCategory != "Q":
    nextCategory = input("Response: ")
    count += 1
    if nextCategory == "A":
        catA = catA + 1
    if nextCategory == "B":     # Changed
        catB = catB + 1
    if nextCategory == "C":     # Changed
        catC = catC + 1

count -= 1
print(catA, catB, catC)
print(catA/count *100, catB/count *100, catC/count *100)
