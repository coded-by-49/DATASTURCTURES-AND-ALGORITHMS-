def reverse_list(lst: list):
    return lst[::-1]

def reverse_list2(lst: list):
    reversed = []
    for i in range(1,len(lst)+1):
        reversed.append(lst[-i])
    return reversed


lst = ["amen", "slawn said."]
for i in reversed(lst):
    print(i)
# print(list(reversed(lst)))

