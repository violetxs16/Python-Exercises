#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first.
#Easy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past_numbers = {}
        #approach: put seen numbers in dictionary. Subtract the target
        #minus the current number and see if result is in dictionary
        for i in range(len(nums)):
            if ((target - nums[i]) in past_numbers):
                if(past_numbers[(target - nums[i])] != i):
                    return [past_numbers[(target - nums[i])], i]
            else:
                past_numbers[nums[i]] = i