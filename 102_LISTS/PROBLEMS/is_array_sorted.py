# i will check if the array is sorted in descending or ascending order
# if neither are meet , i will return zero 





class Solution:
    def isSorted(self,arr,n):
        # return one if all ()
        descend_sorting = 1
        ascend_sorting = 1
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                descend_sorting = 0

            if arr[i]>arr[i+1]:
                ascend_sorting = 0
    
        return 1 if (ascend_sorting == 1 or descend_sorting == 1) else 0
        

example = Solution()

print(example.isSorted([1,1,22,4,7],5))

1,2,3,3,4,7,2
22,5,5,2,33