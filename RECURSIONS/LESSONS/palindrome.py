# A recursive Python program
# to check whether a given
# number is palindrome or not

def isPalRec(st, s, e) :
	# base cose
	if (s == e):
		return True
	# base case --> it is not a palindrome if the element at its corresponding index doesn't match 
	if (st[s] != st[e]) :
		return False

	if (s < e + 1) :
		# this helps us slide through our string from front- center and back to center 
		return isPalRec(st, s + 1, e - 1);

	return True

def isPalindrome(st) :
	n = len(st)
	
	if (n == 0) :
		return True
	
	return isPalRec(st, 0, n - 1);


st = "geeg"
if (isPalindrome(st)) :
	print("Yes")
else :
	print("No")




