#Valid Palindrome 2
#Easy
#Two pointer approach
#Problem:Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def validPalindrome( s: str) -> bool:
    #Two pointer approach
    #Start at front and end
    #Check if palindrome letter by letter
    #   -if letters differ: exclude one letter at a time & check if palindrome
    if len(s) == 1:
        return True
        
    start = 0
    end = len(s) - 1
    while(start < end):
        if s[start] == s[end]:
            print(s[start] + s[end])
            start += 1
            end -= 1
        else:
            end -= 1
            if helper(s,start,end) == True:
                return True
            end += 1
            start += 1
            if helper(s,start, end) == True:
                return True
            else:
                return False
    return True
def helper( s: str, start: int, end: int) -> bool:
    while(start < end):
     #   print(s[start] + s[end])
        if s[start] == s[end]:
            print(s[start] + s[end])
            start += 1
            end -= 1
        else:
            return False
    return True
print(validPalindrome("abc"))