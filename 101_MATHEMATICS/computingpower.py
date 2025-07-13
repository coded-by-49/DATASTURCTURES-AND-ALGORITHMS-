#naive approach
def computingpower(x,n):
    a = 1
    for i in range(n):
        a *= x
    return a

def power(x, y):
	temp = 0
	if(y == 0):
		return 1
	if (y % 2 == 0) :
		return power(x, int(y / 2)) * power(x, int(y / 2))
	else:
		return x * power(x, int(y / 2)) * power(x, int(y / 2))

def power2(a,n):
	val = 1
	while (n > 0):
		# if (n % 2 != 0 ):
		if (n & 1): 
			val *= a
		a = a * a
		# n = n//2 
		n >>= 1
	return val




print(power2(2,4))