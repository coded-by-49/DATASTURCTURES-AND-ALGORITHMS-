def _2_max(l):
    largest = l[0]
    for i in l:
      if largest < i:
         largest = i
    l.remove(largest)
    print(l)
    for i in l:
      largest = l[0]
      if largest < i:
         largest = i
    return(largest)


# print(_2_max([1,2,23,45,24,23,21,4930]))


#efficient approach 

def get_2_max(l):
    first = l[0] ; second = None
    for i in l[1:]:
        if first < i:
            second = first
            first = i
        elif first > i and (second == None or i>second):
            second = i
    return second

print(get_2_max([45,24,23,21,]))


def getSecMax(l):
    if len(l) <= 1:
        print("here")
        return None
    lar = l[0]; slar = None

    for x in l[1:]:
        if x > lar:         # if current element is greater than lar(largest element)
            slar = lar          # update slar to largest
            lar = x         # update lar to current element(largest)

        elif x > lar:      # if x is less then largest and not equal to lar(largest element)
            if slar == None or slar < x:    # if x is greater then second largest
                slar = x                    # assign current element is second largest
    print("here")
    return slar

# print(getSecMax([45,24,23,21,]))