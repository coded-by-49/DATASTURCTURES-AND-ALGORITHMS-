def firstandlast(nums:int, x:int):
    first = None
    last = None 
    for i in range(0,len(nums)):
        if (x == nums[i] and first == None):
            first = i
        elif (x == nums[i] and first != None):
            last = i
    if (first == None and last == None):
        print ("Not found")
    else:
        print("First Occurrence = ", first,
			" \nLast Occurrence = ", last)
        
class binarysearch:
    def __init__(self,):
        pass

    def lastoccurence(self, nums : list, x : int, low , high):
        mid = low+(high-low)//2
        low = 0
        high = len(nums)-1
        if (high>= low):
            if nums[mid]==x and (mid == 0 or x < nums[mid+1]):
                return mid 
            
            elif x<nums[mid]:
                return self.lastoccurence(self, nums, low, mid-1)
            else:
                return self.lastoccurence(self, nums, mid+1, high )
        return -1 


test = binarysearch()



        
