def check_prime(n):
    if n == 1:
        return False 
    i = 2 
    while ((i * i)<= n):
        if n%i == 0:
            return False
        i += 1
    return True


def prime_factors(n):
    for i in range(2,n+1):
        if check_prime(i):
            while n%i == 0:
                print(i)
                n //= i

prime_factors(100)