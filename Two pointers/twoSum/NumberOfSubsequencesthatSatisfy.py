#1498. Number of Subsequences That Satisfy the Given Sum Condition
#Medium
#Solution: two pointer approach
#Problem: Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        counter = 0
        nums.sort()
        for i in range(len(nums)):
            num_sum = nums[i] * 2
            if num_sum <= target:
                counter += 1
        
        front = 0
        back = len(nums) - 1
        while(front < back):
            num_sum = nums[front] + nums[back]
            if num_sum <= target:
                counter += 1
            elif num_sum > target:
                back -= 1
        return counter