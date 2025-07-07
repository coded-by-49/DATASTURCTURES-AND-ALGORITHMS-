def rotate(nums:list, k: int):
        n = len(nums)
        temp = [0]*n
        # just incase k is greater n
        k = k%n

        for i in range(k,n):
            temp[i-k] = nums[i]
            print(temp)
        
        for i in range(k):
            temp[n-k+i] = nums[i]

        nums = temp
        return nums
print(rotate([1,2,3,4,5],2))

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

