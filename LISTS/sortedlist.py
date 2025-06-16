def sorted_ornot(lst: list):
    for i in range(len(lst)-1):
        if (lst[i+1]>=lst[i]) == False:
                return False
    return True

print(sorted_ornot([10,20,30,40,40]))
