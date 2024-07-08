Two pointers approach
If we are given an ordered array and we need to find two numbers within that array that match a target, 
we can do the two pointers approach. First, we have a head pointer and a tail pointer.
Second, we see which pattern is matched: 
If the sum of the numbers that the pointers point to is greater than target : move tail to the left
If the sum of the numbers that the pointers point to is less than the target : move head to the right