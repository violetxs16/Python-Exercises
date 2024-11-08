class Solution(object):
    def search(self, nums, target):
        left  = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
#understanding: we are given an array and a target and we are going to return the index of the target in the array, -1 otherwise. Constraint, must peform it in O(log n) tinme. 
#Mtach: array problem, binary search problem
#Plan: peform binary search on the array. 
#left = 0
#right = len(nums) - 1
#while(left  < right):
    #mid = (right - left) // 2
    #if ==, return ,mid
    #if less we move left pointer to mid + 1
    #else, we move right pointer to mid - 1
#return -1

        