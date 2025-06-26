#Given an array arr[] of size N and two elements x and y, use counter variables to find which element appears most in the array. If both elements have the same frequency
# then return the smaller element.


# create two varialbles to store the count 
# one stores the count of the x and the other of y in an array
# now after these two count have been gotten
# i check for two conditions :

# is one count greater than the other 
# are they equal , if so then return the smaller value

class Solution:   
    def majorityWins(self, arr, n, x, y):
        count_x = sum (1 for i in arr if i == x)
        count_y = sum (1 for i in arr if i == y)
        return x if (count_x>count_y or (count_x == count_y and x<y)) else y