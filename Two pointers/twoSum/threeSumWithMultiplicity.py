#3Sum with multiplicity
#Medium
#Two pointer approach
#

def threeSumMulti(arr: list[int], target: int) -> int:
        #Two pointer approach
        #We start one pointer at the start
        #One pointer at the end
        #Move in accordance to the target
        #We fix one of the variables to make the problem 2 pointers approach
        arr.sort()
        tups_counter = 0
        tups = []
        for i in range(len(arr)-2):
            #Need to reset variables at each start
            start = i + 1
            end = len(arr) - 1
            while(start < end):
                #Perform summation
                sum_var = arr[i] + arr[start] + arr[end]
                if sum_var == target:
                    print(str(arr[i]) + str(arr[start]) + str(arr[end]))
                    tups.append((arr[i], arr[start], arr[end]))
                    tups_counter += 1
                    #start += 1
                    #end -= 1
                elif sum_var > target:#move number
                    end -= 1
                else:
                    start += 1
        return tups_counter

arr = [1,1,2,2,3,3,4,4,5,5]
print(threeSumMulti(arr, 8))