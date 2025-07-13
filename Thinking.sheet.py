def search(arr, x):
    right = len(arr)-1
    left = 0
    for _ in range(len(arr)//2+1):
        if arr[left] == x:
            return left
        if arr[right] == x:
            return right
        else:
            left += 1
            right -= 1
        if right == left:
            return -1 


arr = [1, 2, 3, 4, 5]
x = 5

# Function call
print(search(arr, x))