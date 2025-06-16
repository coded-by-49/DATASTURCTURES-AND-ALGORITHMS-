l = [10,10,20,30,40,50,60,70,80]

print(l)
print(l.pop()) # this removes then returns the last item on the list 
# print(l.remove(400)) --- flags an error
print(f"return value of ther remove function: {l.remove(10)}") # removes 10 but returns none and it only removes one occurnce of 10

print(l)
del l[1]
print("after del keyword")
print(l)
del l[0:2]
print("deletion of ffirst two numbers")
print(l)

# we also have: (these functions must contain all integers or all letters(now it shifts to lexographicall implementation))
max(l)  # lexo
min(l)  # lexo
sum(l)
l.reverse() # lexo
l.sort()  # lexor


# we also have the reversed function that transforms the list into
# an iterator


