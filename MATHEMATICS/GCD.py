def hcf ( a, b ):
    lowest = a if a<b else b # get the lowest number
    hcf = 1 # give the hcf a starting value
    for i in range(1,lowest):  # transverse through the lowest digit
        if (a%i == 0 and b%i == 0): # find the one that is a factor of both of them
            hcf = i # that becomes the current hcf, unitl a better value is reached
    return hcf
# print(hcf(26,65))

def hcf2(a,b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a==b):
        return a
    higher = a if a>b else b
    lower = a if a<b else b

    if (higher % lower == 0):
            return lower
    
    print(f"higher ({higher}) - lower({lower})")
    return(hcf2(higher-lower,lower))    

print(hcf2(8,2))