#Boats to save people
#Medium
#Two pointer approach
#Problem: You are given an array people where people[i] is the weight of the ith person, 
#and an infinite number of boats where each boat can carry a maximum weight of limit. 
#Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
#Return the minimum number of boats to carry every given person.
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        start = 0
        end = len(people) - 1
        while(start <= end):
            weight = people[start] + people[end]
            if weight <= limit:#Both people can go together
                start += 1
                end -= 1
                boats += 1
            else:#Heaviest person goes alone
                end -= 1
                boats += 1
        return boats