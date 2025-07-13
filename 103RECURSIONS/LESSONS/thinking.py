def dup(lst: list) -> bool:
    for item in lst:
        counter = 1
        for i in range(lst.index(item)+1,len(lst)):
            if item == lst[i]:
                counter += 1
            if counter == 2:
                return True
    return False
            

#effecient method m

def dup(lst: list) -> bool:
    checked_set = set() # we want to store any number we have checked here 
    for i in lst:
        if i in checked_set:
            return True
        #but if is already in checked_set, which doesn't accept duplicates 
        checked_set.add(i)
    return False

print(dup([2,3]))