a = ['Learn', 'Quiz', 'Practice', 'Contribute'] 
b = a 
c = a[:] 

b[0] = 'Code'
c[1] = 'Mcq'

count = 0
for i in (a, b, c): 
	if i[0] == 'Code': 
		count += 1
	if i[1] == 'Mcq': 
		count += 10

print (count) 