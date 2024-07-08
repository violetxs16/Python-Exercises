#Two Sum
#Easy
#Two pointers approach
#Problem: Given an ordered array and a target, find a pair in the array whose sum matches the target
#Time complexity: O(N)
def twoSum_pointers(arr, target) -> [int]:
    head_pos = 0
    tail_pos = len(arr) - 1
    while(head_pos != tail_pos):
        pair_sum = arr[head_pos] + arr[tail_pos]
        if pair_sum == target:#Match is found
           return [head_pos,tail_pos]
        elif pair_sum > target: #Pair sum is greater than target, move tail left
            tail_pos -= 1
        else:#Pair sum is less than target, move head right
            head_pos += 1
    return [0,0] #No pair found

print(twoSum_pointers([1,2,3,4,5,6],6))