#3Sum
#Medium
#Two pointers approach
#Problem: Given an array of nums, return all triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, j != k
#and the values add up to zero. There should be no duplicate triplets
#O(N^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #Sort array
        triplets = []
        for i in range(len(nums) - 2): #Fixing value i
            j = i + 1
            k = len(nums) - 1
            while(j < k): #Two pointers method
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == 0:#Match found
                    if([nums[i],nums[j],nums[k]] not in triplets):#Checking duplicates in array
                        triplets.append([nums[i], nums[j], nums[k]])
                if sum3 > 0:
                    k -= 1
                else:
                    j += 1
        return triplets
    Solution.threeSum([-1,0,1,2,-1,-4])