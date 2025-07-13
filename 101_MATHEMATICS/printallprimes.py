def check_prime1(n):
    if n == 1:
        return False 
    i = 2 #iterator 
    while ((i * i)<= n):
        if n%i == 0:
            return False
        i += 1
    return True

def allprimenumbers(n):
    if n == 1 :
        print(i)
    else:
        for i in range (2,n+1):
            if (check_prime1(i)):
                print(i)


#seive of Eratosthenes

def SieveOfEratosthenes(num):
    p = 2
    prime = [True for i in range(num+1)]

    while (p*p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p): # change all the multiples of p from its square,becase p(2)is a prime number in the first place
                prime[i] = False
        p += 1
    
    for p in range(2, num+1):
        if  prime[p]:
            print(p)
