def myfactorial(number):
    if (number == 0 or number == 1):    # base case
        answer = 1
    else:
        answer = number * myfactorial(number-1)
    return answer

print(myfactorial(4))
