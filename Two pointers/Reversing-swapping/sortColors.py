#Sort Colors
#Medium
#Regular approach
#Problem: Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#You must solve this problem without using the library's sort function.

def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Two pointer approach
        zero = 0
        one = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
        for i in range(len(nums)):
            if i < zero:
                nums[i] = 0
            elif i >= zero and i < one+zero:
                nums[i] = 1
            else:
                nums[i] = 2
        
