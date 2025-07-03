# the intruction is to retrieve the index of a number in a sorted list and if the number isn't there we return -1

class solution:
    def linear_search(self,x: int, nums : list) -> int:
        nums.sort()
        for i in nums:
            if i == x:
                return nums.index(i)
        return -1
     # now we use binary search 
    def binary_search(self, x: int, nums : list) -> int:
        nums.sort

        low = 0
        high = len(nums)-1
        mid_point = (low+high)//2

        while low <= high:
            if x == nums[mid_point]:
                return mid_point 
            
            elif x > mid_point:
                low = mid_point+1
                
            else:
                high = mid_point-1
        return -1
            
    
trial = solution()

print(trial.find_index(4,[1,2,3,4,5,6]))
            
