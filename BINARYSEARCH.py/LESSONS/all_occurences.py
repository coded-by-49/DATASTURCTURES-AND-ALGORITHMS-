def left_occurences(nums, x, n, low, high):
    low = 0 
    high = n-1
    mid = (low+high)//2
    occurences = 0 
    while low<=high:
        