def dup(lst: list) -> bool:
    for item in lst:
        counter = 1
        for i in range(lst.index(item)+1,len(lst)):
            if item == lst[i]:
                counter += 1
            if counter == 2:
                return True
    return False
            

print(dup([1,2,3,4]))
