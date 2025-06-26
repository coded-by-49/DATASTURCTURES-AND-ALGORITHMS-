def print1toN(n):
    if n == 0:
        return "amen"
    print1toN(n - 1) # recurses until it hits a base case, after which it unwinds from the last entry(UNFOLDING)
    print(n) # which is 1->2 -> 3 ....

print1toN(10)

def print1toN(n):
    if n == 0:
        return "amen"
    print(n) 
    print1toN(n - 1) # recurses until it hits a base case, after which it unwinds from the last entry
    #Even though it may look like there’s “nothing to do” after the recursive call, Python still unwinds the call stack — because it must.
print1toN(10)