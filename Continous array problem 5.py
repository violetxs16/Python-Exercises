
#Fruits into baskets
#Difficulty: Medium
#Given an array of characters where each character represents a fruit tree, 
#you are given two baskets and your goal is to put maximum number of fruits in each basket. 
#The only restriction is that each basket can have only one type of fruit.

#Solution: Sliding window approach
#Time complexity: O(n)



def fruitIntoBaskets(fruit_arr):
    baskets = {}
    start_index = 0
    max_num_fruits = 0
    for i in range(len(fruit_arr)):
        fruit = fruit_arr[i]
        if fruit not in baskets and len(baskets) == 2:
            #Delete first fruit
            delete_fruit = fruit_arr[start_index]
            start_index += 1
            del baskets[delete_fruit]
            baskets[fruit] = 1
        else:
            if fruit in baskets:#Fruit is already in basket
                baskets[fruit] += 1 
            else:#Adding new fruit
                baskets[fruit] = 1
        #Sum all values in the dictionary
        sum_values = 0
        for key in baskets:
            sum_values += baskets[key]
            
        if (sum_values > max_num_fruits):
            max_num_fruits = sum_values

    return max_num_fruits

Fruit=['A', 'B', 'C', 'A', 'C']
print(fruitIntoBaskets(Fruit))

Fruit2=['A', 'B', 'C', 'B', 'B', 'C']
print(fruitIntoBaskets(Fruit2))