input_list = [1,2,19,20,39,40,50]

even =  [i for i in input_list if i % 2==0]
print(even)
odd =  (i for i in input_list if i % 2!=0)
for i in odd:
    print(i)