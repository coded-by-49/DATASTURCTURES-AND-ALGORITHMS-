def cnt(n):
    i = 0
    while n>0:
        i += 1
        n = n//10
        print(n)
        print(f"{i} \n")
    return i 

print(cnt(9542))
