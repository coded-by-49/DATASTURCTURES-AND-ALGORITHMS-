def evenandodd(list):
    even = []
    odd = []
    for _ in list:
        if (_%2 == 0):
            even.append(_)
        elif (_%2 != 0):
            odd.append(_)
    return f"These are the even numbers {even}\nThese are the odd numbers {odd}"

print(evenandodd([3,4,5,7,28,19]))