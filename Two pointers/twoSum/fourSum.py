#fourSum
#Medium
#Two pointers approach
#Problem: Given an array of nums of n integers, return an array of all unique quadruplets[nums[a], nums[b], nums[c], nums[d]] such that:
#       0 <= a, b, c, d < n
#       a, b, c, and d are distinct.
#       nums[a] + nums[b] + nums[c] + nums[d] == target
#       You may return the answer in any order. 

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = []
        nums.sort()
        #Two pointer approach
        #Must set a and b
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c = b + 1
                d = len(nums) - 1
                while(c < d):
                    quad_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    nums_list = [nums[a],nums[b],nums[c],nums[d]]
                    if (quad_sum == target) and nums_list not in quadruplets: #No duplicates
                        quadruplets.append(nums_list)
                       # d -= 1
                        c += 1
                    elif (quad_sum > target):#Move d left
                        d -= 1
                    else: #Move c right
                        c += 1
        return quadruplets