def reversed_list(lst):
    item = []
    counter = 0
    for i in lst:
        counter +=1
        item.append(lst[len(lst)-counter])
    return item

# print(reversed_list([1,2,3,4,5]))


def geeks_version(l):
    s = 0 # start 
    e = len(l)-1 # end

    while e > s: 
        print(f"this is the value of e-{e} and this is the value of s-{s}")
        l[s], l[e] = l[e], l[s]  # swapping left element to right and right element to left
        # l[s] = l[e] ; l[e] = l[s] #this will assign one statement after the other
        s = s + 1
        e = e - 1

user_input = "1 2 3 4 5 6"  # Example input with spaces
l = [int(x) for x in user_input.split()]  # convert input string into a list of integers
geeks_version(l)
print("Reversed list:", l)  # Output the reversed list