#remove Element
#Easy
#Approach: Two pointers
#Problem: Given an unsorted array and a key, remove all instances of the key
def removeElement(arr, key) -> list:
    non_duplicates = 0
    for i in range(len(arr)):
        if arr[i] == key:#Found key
            continue
        else:
            arr[non_duplicates] = arr[i]
            non_duplicates += 1
    return arr[:non_duplicates] #Splice off remaining elements
test_array = [1,1,1,2,2,3,3,7,7,9]
print(removeElement(test_array,3))