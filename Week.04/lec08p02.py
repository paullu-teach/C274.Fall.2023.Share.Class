place = {}
place["Canada"] = "Alberta"
place["Netherlands"] = "Zeeland"
place["USA"] = [ "California", "New York" ]
place["United Kingdom"] = [ "England", "Wales" ]
place["Italy"] = [ "Calabria", "Liguria" ]
print("place:  ", place)
print()

for i in place.keys():
    print(i)
print()
for i in place.values():
    print(i)
