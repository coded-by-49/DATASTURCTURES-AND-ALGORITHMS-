# Given an array arr[] of size N containing positive integers and an integer X, find the element in the array which is smaller than X and closest to it.


class Solution:
    def immediateSmaller(self,arr,n,x):
        # the number with the greatest remainder after a modular division with x, is the closet it

        
        # we are setting greatest remainder to -1 in case x <= i in arr
        greatest_remainder = -1
        for i in arr:
            if i < x:
                if greatest_remainder < i%x:
                    greatest_remainder = i%x
        return greatest_remainder