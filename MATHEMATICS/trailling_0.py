def zeros(a): # the value of the factorial, has to be passed 
    # native method, 
    stop = False 
    c = 0
    while not stop:
        if (a % 10 == 0):
            c += 1
            a = a // 10
        else:
            return c 

def find_trailing_zeros(n):
    if n < 0:  # Negative Number Edge Case
        return -1

    # Initialize result
    count = 0

    # Keep dividing n by powers of 5 and update count
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5

    return count

# Driver Code
if __name__ == "__main__":
    n = 767
    print(f"Count of trailing 0s in {n}! is {find_trailing_zeros(n)}")

