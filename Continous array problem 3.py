#1.2 Smallest Subarray with a given sum (easy)

#Given an array of positive integers and a positive integer S, find the length smallest 
#continous subarray that is greater than or equal to s

def length_continous_subarray(arr, s):
    #we are going to use the sliding window approach
    #we have overall sum: add from the back(slide foward) we decrease from front(element passed)
    #keep track of smallest length
    #keep track of window start - start position of index

    #approach: we are seeing if the sum is greater than s, if true we shrink the window until
    #we are less than s, if false we continue adding to the overall sum
    if s == 0 or len(arr) == 0: return 0
    sum_arr = 0
    len_subarr = len(arr) #if we can not find a continous subarray that meets conditions we return zero
    index_start = 0

    for i in range(len(arr)):
        sum_arr += arr[i]
            #decrease window size until condition is false: keep track of length & start?
        while(sum_arr >= s):
            if (i - index_start) < len_subarr:
                len_subarr = (i - index_start+1)
                #print(len_subarr)
                #slowly shrink window size
            sum_arr -= arr[index_start]
            index_start += 1
   # print(len_subarr)
    return len_subarr

arr = [2, 3, 4, 1, 5]
print(length_continous_subarray(arr, 7))
arr = [2, 1, 5, 1, 3, 2]
print(length_continous_subarray(arr, 3))
        

