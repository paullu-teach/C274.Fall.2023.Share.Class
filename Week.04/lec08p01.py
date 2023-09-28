food = {}
food["Toad in a Hole"] = "England"
food["Pizza"] = "Italy"
food["Xiao Long Bao"] = "China"
food["Poutine"] = "Canada"
food["Haggis"] = "Scotland"
print("food:  ", food)
print()

food2 = { "Xiao Long Bao":"China", "Pizza":"Italy", "Poutine":"Canada", "Toad in a Hole":"England", "Haggis":"Scotland" }
print("food2: ", food2)
for i in food2.keys():
    print(i)
print()
for i in food2.values():
    print(i)
