# Join

fA = open("./fileA08.txt", "r")
in_A = fA.readline()

kv_A = {}
while in_A:
    a = in_A.strip().split(",")
    key = a[0]
    kv_A[ key ] = ",".join(a[1:])
    in_A = fA.readline()
fA.close()
#print(kv_A)

fB = open("./fileB08.txt", "r")
in_B = fB.readline()

while in_B:
    b = in_B.strip().split(",")
    key = b[0]
    if key in kv_A:
        vals = ",".join(b[1:])
        print(key+","+kv_A[key]+","+vals)
        del kv_A[key]
    in_B = fB.readline()

fB.close()
