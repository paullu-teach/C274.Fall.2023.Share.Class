fA = open("./A.txt")
fB = open("./B.txt")

in_A = True
in_B = True

while in_A and in_B:
    in_A = fA.readline()
    in_B = fB.readline()
    a = in_A.strip()
    b = in_B.strip()
    print(a,b)

fA.close()
fB.close()

# Originally lec07base.py
