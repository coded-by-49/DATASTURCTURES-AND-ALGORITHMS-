lst = [1,2,3,4,5]
l2 = lst[0:4]

print(l2)

def insertAtEnd(arr,sizeOfArray,element):
    return arr[:len(arr)]+[element]