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
                # to be continued