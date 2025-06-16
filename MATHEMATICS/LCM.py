from GCD import hcf2

def lcm(a,b):
    higher = a if a>b else b
    
    while not (higher%a == 0 and higher%b == 0):
        higher += 1 
    return higher

def lcm2(a,b):
    return a*b//hcf2(a,b)