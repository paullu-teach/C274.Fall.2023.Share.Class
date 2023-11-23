import pickle

d = dict()
d[ "cat" ] = 2
d[ "dog" ] = 7

e = dict()
e[ "hotdog" ] = 8
e[ "hamburger" ] = 9

print("Dump:", d)
print("Dump:", e)
with open("cd.picklev2", "wb") as fout:
    pickle.dump(d, fout, protocol=4)    # Older protocol for compatibility
    pickle.dump(e, fout, protocol=4)    # Older protocol for compatibility
