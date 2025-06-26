def rotate(nums:list, k: int):
        nums = nums[k+1:]+nums[:k+1]
        return nums

def rotate_array(nums:list[int], k : int):
    #rotate the whole array
    start = 0; end= len(nums)-1
    while end>start:
        nums[end],nums[start] = nums[start],nums[end]
        end -= 1
        start += 1
    #rotate the first k-1 elements        
    start = 0; end= k-1
    while end>start:
        nums[end],nums[start] = nums[start],nums[end]
        end -= 1
        start += 1
    #rotate remaining parts of the array
    start = k; end= len(nums)-1
    while end>start:
        nums[end],nums[start] = nums[start],nums[end]
        end -= 1
        start += 1
    return nums


print(rotate_array([1,2,3,4,5,6,7,8],4))