def removeDuplicates(lst: list, n: int):
    single_ver = []
    single_ver.append(lst[0]) # the first element is not a duplicate
    item_added = 1 

    for i in range(1,n):   # i could also loop through a sliced version of the list
        if single_ver[item_added-1] != lst[i]: # we get the index of the already added item and compare it with next item on the list
           single_ver.append(lst[i])     
           item_added += 1
    
    return item_added
# n = 7  # Size of the array
# arr = [10, 20, 20, 30, 30, 30, 30]  # Input array with duplicates
# print(removeDuplicates(arr, n))  # Call the function and print the number of unique elements



def removeDuplicates2(lst: list, n: int):
    j = 0
    while j+1<n:
        if lst[j] == lst[j+1]:
            lst.pop(j+1)
            n -= 1
        elif lst[j] != lst[j+1]:
            j += 1
    return j+1

n=7
arr=[10, 20, 20, 30, 30, 30, 30]
# print(removeDuplicates2(arr, n))

