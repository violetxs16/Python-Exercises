#Reverse String
#Easy
#Two pointer approach
#Write a function that reverses a string. The input string is given as an array of characters s.
#You must do this by modifying the input array in-place with O(1) extra memory.
def reverseString( s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        while(start < end):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1