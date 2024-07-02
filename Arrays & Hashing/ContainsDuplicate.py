#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#Easy
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = {}
        for i in range(len(nums)):
            if nums[i] in elements:
                return True
            elements[nums[i]] = 1 #Adding element to dictionary

        return False
         