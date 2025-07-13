'''Given a sorted array arr[] with possibly duplicate elements, the task is to find indexes of 
the first and last occurrences of an element x in the given array.

Order Matters in conditions:
In A or B, if A is True, B is never evaluated.

In A and B, if A is False, B is never evaluated.
'''

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

class Binarysearchimplemenation:
    def firstoccurence(self, nums:list, target):
        start = 0
        end = len(nums)-1
        while start <= end:
            middle = start + (end - start)//2
            if nums[middle] == target and (nums[middle]>nums[middle-1] or middle == 0):
                return middle 
            elif target > nums[middle]:
                start = middle + 1
            else:
                end = middle - 1
        return -1
    def lastoccurence(self, nums:list, target):
        start = 0
        end = len(nums)-1
        while start <= end:
            middle = start + (end - start)//2
            if nums[middle] == target and (middle == len(nums)-1 or nums[middle]<nums[middle+1]):
                return middle
            elif target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        return -1
     


testing = Binarysearchimplemenation()
arr = [1, 1, 1, 2, 2, 2, 4, 7, 8, 8]
# print(testing.firstoccurence(arr,2))
print(testing.lastoccurence(arr,8))