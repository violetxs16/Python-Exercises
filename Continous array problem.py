#Problem: Given a array, find the average of all contiguous subarrays of size ‘5’ in the given array
#Approach: Sliding window

#Keep track of overall sum of 5 current element
#Keep track of start and end positions to maintain k elements per avg
def avg_subarrays(arr, k):
    result = []
    sum = 0
    start = 0

    # 1-> 2-> 3->4 -> 5 then 2->3->4->5->6 & so on
    #We only add avg when end is >= k - 1
    for end in range(len(arr)):
        sum += arr[end]
        if(end >= k - 1): #if k = 5, condition will be 5-1 = 4, so end must be 4 for condition to be true
            result.append(sum / k)
            sum -= arr[start] #We are subtracting the element we are passing
            start += 1
    return result

arr = [2, 3, 4, 1, 5]
print(avg_subarrays(arr, 2))
arr = [2, 1, 5, 1, 3, 2]
print(avg_subarrays(arr, 3))
           