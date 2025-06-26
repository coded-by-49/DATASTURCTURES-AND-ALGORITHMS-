def sumofdigits(n):
    if n<1:
        return 0
    # we are recursivly adding the last of a number and cutting it off after
    return n%10 + sumofdigits(n//10)


print(sumofdigits(12345))
