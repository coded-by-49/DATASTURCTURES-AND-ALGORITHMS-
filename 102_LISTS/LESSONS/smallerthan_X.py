def smallerthan_x(lst,x):
    smaller = []
    for i in lst:
        if i < x:
            smaller.append(i)
    return (smaller)

print(smallerthan_x([232,44,1,2,3,4,5,6],10))