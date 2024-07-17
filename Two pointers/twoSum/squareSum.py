#Sum of square numbers
#Medium
#Two pointer approach
#Problem: Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #two sum approach
        #a^2 + b^2 = c
        start = 0
        end = c ** 2
        while(start <= end):
            squareSum = start ** 2 + end ** 2
            if squareSum == c:
                return True
            elif squareSum > c:
                end -= 1
            else:
                start += 1
        return False