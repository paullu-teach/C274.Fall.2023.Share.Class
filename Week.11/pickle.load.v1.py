import pickle

with open("cd.pickle", "rb") as fin:
    d = pickle.load(fin)

print("Load: ", d)
