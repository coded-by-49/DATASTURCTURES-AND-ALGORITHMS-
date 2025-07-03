def R_binary(nums:list, x: int, low: int, high: int) -> int :
    mid_point = (low+high)//2
    if nums[mid_point] == x :
        return mid_point
    elif low > high :
        return -1 
    elif x>nums[mid_point] :
        return R_binary(nums, x, mid_point+1, high)
    else:
        return R_binary(nums, x, low, mid_point-1)

nums = [10,20,30,40,50,60,70,80]

print(R_binary(nums,100,0,len(nums)-1))