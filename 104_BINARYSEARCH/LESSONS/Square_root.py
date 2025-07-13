def squareroot(num):
    if num == 0 or num == 1:
        return num
    i = 2
    while i * i <= num:
        if i * i == num:
            return i
        i += 1
    return i - 1

def binary_search (num):
    if num == 0 or num == 1:
        return num
    lower_b = 1 
    upper_b = num//2

    while lower_b <= upper_b:
        print(f"This is the lowerboundary {lower_b}\nThis is the upperboundary {upper_b}")
        mid = lower_b + (upper_b - lower_b)//2
        print(f"This is the current mid value {mid} \n")

        if (mid*mid == num):
            print(f"found at {mid}")
            return mid
        
        if (mid * mid < num):
            lower_b = mid + 1
            ans = mid # we want to keep track of the last number (mid-value) that its square is closest to our number

        else:
            upper_b = mid-1

    return ans

print(binary_search(16))