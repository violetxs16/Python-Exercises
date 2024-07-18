#Reverse only letters
#Easy
#Two pointer approach
#Problem: Given a string s, reverse the string according to the following rules:
#All the characters that are not English letters remain in the same position.
#All the English letters (lowercase or uppercase) should be reversed.
#Return s after reversing it.

def reverseOnlyLetters(s: str) -> str:
        #Two pointer approach
        #   -Check if character is a letter
        start = 0
        end = len(s) - 1
        reverse_str = list(s)
        while(start < end):
            if reverse_str[start].isalpha() and reverse_str[end].isalpha():
                temp = reverse_str[start]
                reverse_str[start] = reverse_str[end]
                reverse_str[end] = temp
                start += 1
                end -= 1
            elif not reverse_str[start].isalpha():
                start += 1
            else:
                end -= 1
        return ''.join(reverse_str)