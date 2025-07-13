def oneoddoccuring(lst : list):
    for _ in lst:
        check = _
        count = 0
        for i in range(lst.index(check),len(lst)):
            if _ == lst[i]:
                count += 1
        if (count%2 != 0):
            return _
        

arr = [4,3,4,4,4,5,5,3,3]            
print(oneoddoccuring(arr))


#loop through a list 
#select one item at a time 
# get the first occurrence of that item 
# loop from there and when you encounter a value equivalent to it, you increase the count


