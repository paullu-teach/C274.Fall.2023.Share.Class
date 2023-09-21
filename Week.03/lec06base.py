import random

def uniqueRandomInt(l,u,target):
    assert (u-l+1) >= target, "Not enough range"
    count = 0
    theNums = []
    while count < target:
        n = random.randint(l,u)
        if n in theNums:
            pass
        else:
            theNums.append(n)
            count += 1
    return theNums

if __name__ == "__main__":
    random.seed(10)
    print(uniqueRandomInt(0,3,2))
    print(uniqueRandomInt(6,15,5))
    print(uniqueRandomInt(1,50,5))

    # WRONG CALLING SEMANTICS print(uniqueRandomInt(6,15,50))
