import random

def uniqueRandomInt(l,u,target):
    count = 0
    theNums = []
    while count < target:
        n = random.randint(l,u)
        if n not in theNums:
            theNums.append(n)
            count += 1
    return theNums

if __name__ == "__main__":
    print(uniqueRandomInt(0,3,2))
#    print(uniqueRandomInt(6,9,5))
    print(uniqueRandomInt(1,50,5))

# Originally lec06base.py
#    assert (u-l+1) >= target, "Not enough range"
#    random.seed(10)
