#Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

#How to approach? Sliding window approach
#Have an overall sum as we progress through the array
#Have condition to test if end position >= k - 1, since after that we will be documenting the avg
#       -Subtract passed value from sum
#       -Increase start by 1
#Have variable max_sum to contain maximum sum of continous array of size k

def max_continous_arr(arr, k):
    sum = 0
    max_sum = 0
    start = 0
    for end in range(len(arr)):
        sum += arr[end]
        if(end >= k - 1):#ex. end = 4 & k = 5: conditon = 4 TRUE --> We have k continous elements
            if(sum > max_sum):
                max_sum = sum
            sum -= arr[start] #We are sliding window over by one index, start index is left behind
            start += 1 #Record new start of continous sub array of size k
    return max_sum

arr = [2, 3, 4, 1, 5]
print(max_continous_arr(arr, 2))
arr = [2, 1, 5, 1, 3, 2]
print(max_continous_arr(arr, 3))