import pickle

d = dict()
d[ "cat" ] = 2
d[ "dog" ] = 7

print("Dump:", d)
with open("cd.pickle", "wb") as fout:
    pickle.dump(d, fout, protocol=4)    # Older protocol for compatibility
