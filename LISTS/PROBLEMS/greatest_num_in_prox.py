#User function Template for python3

class Solution:
    # inf has been imported in driver code
    def immediateGreater(self,arr,n,x):
        # result = -1 
        # check for the elements greater than x
        # check for the least amongst them, that is the answer
        result = -1 
        for i in arr:
            if i>x:
                if (result == -1):
                    result = i # first element that is greater x
                if result > i:
                    result = i # change element if there is another element that is greater than x but less than i
        return result
    

example = Solution()
example.immediateGreater([4,67,13,12,15],5,16 )