def nCr(n,r):
    if r == 1 or r == n:
        return 1
    return nCr(n-1,r-1)+nCr(n-1)
    