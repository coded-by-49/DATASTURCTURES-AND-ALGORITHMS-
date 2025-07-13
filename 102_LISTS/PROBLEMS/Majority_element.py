'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
 
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        distinct_values = set(nums)
        for i in distinct_values:
            if nums.count(i)>len(nums)/2:
                return i 
    def majorityElement2(self, nums: List[int]) -> int:
        numbers = {}
        for i in nums:
            if i not in numbers:
                numbers[i] = 1
            else:
                numbers[i] += 1
            if numbers[i] > len(nums)//2:
                return i