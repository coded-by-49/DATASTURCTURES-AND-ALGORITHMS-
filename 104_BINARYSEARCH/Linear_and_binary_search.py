# the intruction is to retrieve the index of a number in a sorted list and if the number isn't there we return -1

class solution:
    def linear_search(self,x: int, nums : list) -> int:
        for i in nums:
            if i == x:
                return nums.index(i)
        return -1
    def optimised_linear_search(self, x:int, nums: list) -> int:
        right = len(nums)-1
        left = 0
        for _ in range(len(nums)//2+1):
            if nums[left] == x:
                return left
            if nums[right] == x:
                return right
            else:
                left += 1
                right -= 1
            if right == left:
                return -1 
    def binary_search(self, x: int, nums : list) -> int:
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
            
