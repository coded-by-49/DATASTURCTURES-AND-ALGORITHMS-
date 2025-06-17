# Given an unsorted array arr[] of size N containing non-negative integers. 
# You will also be given an integer X, the task is to count the number of elements which are strictly smaller than X. 
# The given integer may or not be present in the array given

# brute force
class Solution:
    def smallerThanX(self,arr,n,x):
        # we are using a list generator to generate one for each element that is greater less than i , then summing everything together
        return sum(1 for i in arr if x > i) 
    



example = Solution()
print(example.smallerThanX([1,2,3,4,5,6],6,7))