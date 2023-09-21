f = open("./fileA.txt")
in_A = f.readlines()
f.close()
f = open("./fileB.txt")
in_B = f.readlines()
f.close()
# print(in_A)
# print(in_B)


all_input = zip(in_A,in_B)
for a, b in all_input:
    a = a.strip()
    b = b.strip()
    print(a,b)

# for i in range(len(in_A)):
#    a = in_A[i].strip()
#    b = in_B[i].strip()
#    print(a,b)
