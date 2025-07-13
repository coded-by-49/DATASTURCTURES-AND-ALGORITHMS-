# this is accessing two indicies on the list whilst simultaneously exchaning the value
# this continues until the start enchors the median / medians of the list (when start == end or when start > end), hence the condition end>start

def reverseArray(arr,n):
    start = 0 ; end = n-1
    while end>start:
        arr[start],arr[end] = arr[end],arr[start]  
        start += 1
        end -= 1
    return arr

print(reverseArray([1,2,3,4,5,6,7], 7))
