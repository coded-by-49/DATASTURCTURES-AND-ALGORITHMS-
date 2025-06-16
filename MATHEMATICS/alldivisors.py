# Given a natural number n, print all distinct divisors of it.

# this is a brute force solution 
def alldivs(n):
    print(1)
    # for all numbers from 2-n
    for i in range(2,n):
        if (n % i == 0): # if it is div
            print(i)
    print(n)


def alldivs2(n):
    i = 1
    while (i*i) <= n:
        if (n%i == 0):
            print(i)
            if (i!= n/i):
                print(n//i)
        i += 1


def alldivs_sorted(n):
    i = 1
    while (i*i) <= n:
        if (n%i == 0):
            print(i)
        i+=1
    while(i>=1):
        if (n%i == 0):
            print(n//i)
        i -= 1

alldivs_sorted(30)