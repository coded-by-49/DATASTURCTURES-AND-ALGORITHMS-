def rotateArr1(arr, d):
        #Your code here
        d = d%(len(arr)) # if d is higher than the length
        arr = arr+arr[:d]
        for i in range(d):
            arr.pop(0)

        return arr
def rotateArr(arr, d):
        #Your code here
        d = d%len(arr)
        arr = arr[d:len(arr)-1]+arr[:d]

        return arr

# print(rotateArr([1,2,3,4,5,6], 3))
# the goal of this function is to rotate the first (d) digits in the left to the right

def rotateArr2(arr, d):
    n = len(arr)

    # Handle case when d > n
    d %= n
    
    # Storing rotated version of array in a new list
    temp = [0] * n

    # in all cases the number of items to moved from the right in order to make d digits 
    # go to the LEFT IS len(list)-d, and the index is i+d when i is incrementing from 0->len(list)-d
    for i in range(n - d):
        temp[i] = arr[d + i]

    # Copy the first d(the ones we want to take to the left) elements to the back of temp
    # now i am simply starting from where i stopped, and added the remaining 
    for i in range(d):
        temp[n - d + i] = arr[i]

    return temp

    


# Python Code to left rotate an array using Reversal Algorithm


# Python Code to left rotate an array using Reversal Algorithm

# Function to rotate an array by d elements to the left
def rotateArr(arr, d):
    n = len(arr)

    # Handle the case where d > size of array
    d %= n

    # Reverse the first d elements
    print(f"this is the list - {arr}\n")
    reverse(arr, 0, d - 1)
    print(f"this is the array 1 reverse - {arr} \n")
    # Reverse the remaining n-d elements
    reverse(arr, d, n - 1)
    print(f"this is the array 1 reverse - {arr} \n")
    # Reverse the entire array
    reverse(arr, 0, n - 1)
    print(f"this is the array 1 reverse - {arr} \n")

# Function to reverse a portion of the array
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    
    rotateArr(arr, d)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")


