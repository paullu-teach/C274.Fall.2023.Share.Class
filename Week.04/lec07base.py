fA = open("./fileA.txt")
fB = open("./fileB.txt")

# Read line by line
in_A = fA.readline()		# line, not lines
in_B = fB.readline()		# line, not lines

while in_A != "" and in_B != "":
    a = in_A.strip()
    b = in_B.strip()
    print(a,b)
    in_A = fA.readline()		# line, not lines
    in_B = fB.readline()		# line, not lines

fA.close()
fB.close()
