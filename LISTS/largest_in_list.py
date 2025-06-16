def getmax(l):
    largest = l[0]
    for i in l:
      if largest < i:
         largest = i
    return largest

# print(getmax([1,2,23,45,24,23,21,4930]))

def getMax(l):
    for x in l:  # iterate for each element
        print(f"this is : {x}")
        for y in l:  # iterate to compare with each element
            print(y)
            if y > x:  # if any element is greater than x, break
                break
        else:  # if loop is exited naturally, no larger element found
            return x
    return None

# Hardcoded list for input "1 2 3 4 5"
l = [1, 2, 3, 4, 5]
print(getMax(l))  # Output: 5