#Reverse words
#Medium
#Two pointer approach
#Problem: Given an input string s, reverse the order of the words.
#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#Return a string of the words in reverse order concatenated by a single space.
#Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

def reverseWords(s: str) -> str:
        words = []
        start_front = 0
        start_back = 0
        end_front = len(s) - 1
        end_back = len(s) - 1
        while(start_front < end_front):
            #Move pointers foward until we find a new word
            while(start_back == ' '):
                 start_back += 1
            while(start_front != ' '):
                 start_front += 1
            while(end_back == ' '):
                 end_back -= 1
            while(end_front != ' '):
                 end_front -= 1
            temp = s[start_back:start_front]
            
            
