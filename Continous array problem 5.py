#Fruits into baskets
#Difficulty: Medium
#Given an array of characters where each character represents a fruit tree, 
#you are given two baskets and your goal is to put maximum number of fruits in each basket. 
#The only restriction is that each basket can have only one type of fruit.

#You can start with any tree, but once you have started you can’t skip a tree. 
#You will pick one fruit from each tree until you cannot, i.e., 
#you will stop when you have to pick from a third fruit type.

#Solution: Sliding window approach

def fruit_into_baskets(fruits):
    current_sum = 0
    max_sum = 0
    start_index = 0
    prev_fruit = 0
    #Count all the individual fruit frequencies 
    fruit_freq = {}
    for i in range(len(fruits)):
        if fruits[i] not in fruit_freq:#Fruit not present
            fruit_freq[fruits[i]] = 1
        else:#Fruit already present
            fruit_freq[fruits[i]] += 1
    
    for i in range(len(fruits)):
        if i > 0 and fruits[prev_fruit] == fruits[i]: #Must have two distinct fruits
            start_index += 1
            continue

        current_sum += fruit_freq[fruits[i]] #Add current fruit value
        prev_fruit = i #New old fruit value
        if i > 2:
            current_sum -= fruit_freq[fruits[start_index]]
            if current_sum > max_sum:
                max_sum = current_sum
            start_index += 1
    return max_sum

Fruit=['A', 'B', 'C', 'A', 'C']
print(fruit_into_baskets(Fruit))

Fruit2=['A', 'B', 'C', 'B', 'B', 'C']
print(fruit_into_baskets(Fruit2))