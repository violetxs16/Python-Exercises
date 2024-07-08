#remove Duplicates
#Easy
#Approach: two pointers
#Problem: Given an array of sorted numbers, return the list with no duplicates. 
#Constraints: You should not use any extra space. 

def removeDuplicates(arr) -> [int]:
    non_duplicate = 1
    i = 1
    while (i < len(arr)):
        if arr[non_duplicate - 1] != arr[i]:#We found a new element
            arr[non_duplicate] = arr[i]
            non_duplicate += 1
        i += 1
    return arr[:non_duplicate]

test_array = [1,1,1,3,4,6,6,6,6,9]
print(removeDuplicates(test_array))