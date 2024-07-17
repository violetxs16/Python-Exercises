#3Sum with multiplicity
#Medium
#Two pointer approach
#

def threeSumMulti(self, arr: List[int], target: int) -> int:
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
                    tups.append((arr[i], arr[start], arr[end]))
                    tups_counter += 1
                    start += 1
                    end -= 1
                elif sum_var > target:#move number
                    end -= 1
                else:
                    start += 1
        return tups_counter
        