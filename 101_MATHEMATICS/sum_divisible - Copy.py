class Solution(object):
    def minSubarray(self, nums, p):
        summation = 0
        sum_to_R =[]
        less_than_R = []
        for i in nums:
            summation += i
        if summation < p:
            return 0
        R = summation % p
        if R == 0:
            return 0 
        if R in nums:
            return 1
        for i in nums:
            if R > i:
                less_than_R.append(i)
        # if len(less_than_R) == 1:
            #  return 1
        if len(less_than_R) > 0:
            inner_counter = 0
            less_than_R.sort(reverse=True)
            list_for_i = less_than_R[:-1]
            for i in list_for_i:
                inner_counter += 1
                for j in range(inner_counter,len(less_than_R)):
                    check_sum = i + less_than_R[j]
                    if R == check_sum:
                        # if i was to append with a tuple how would i go about it
                        sum_to_R.append(i)
                        sum_to_R.append(less_than_R[j])
                        print(sum_to_R)
                        return len(sum_to_R)
                        break 
            else:
                
                return -1
        else:
            return -1


trial1 = Solution()
# print(trial1.minSubarray([3,1,4,2],6))
print(trial1.minSubarray([8,8,7],2))

# there is no number when divide my another number can be greater or equal to the number itself
