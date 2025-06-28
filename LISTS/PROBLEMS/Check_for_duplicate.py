# we are asked to check if any number appears twice in a list
def hasDuplicate(nums: list[int]) -> bool:
    for item in nums: # we transerve through our list 
        counter = 1 # we count the first time we see our number
        for i in range(nums.index(item)+1,len(nums)): # we iterate from index after that number to still the end of the whole list
            if item == nums[i]: # if we encounter the number again we increment our counter
                counter += 1
            if counter == 2: # after which we break 
                return True
    return False # if we all the items are check , then there is no duplicate
