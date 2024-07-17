#Reverse vowels
#Easy
#Two pointer approach
#Problem: Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

def reverseVowels(s: str) -> str:
        #Two pointer approach
        #   -lower all letters
        #   -swap if vowel
        start = 0
        end = len(s) - 1
        vowels = ['a','e','i','o','u', 'A','E','I','O','U']
        word = list(s)
        while(start < end):
            if word[start] in vowels and word[end] in vowels:
                temp = word[start]
                word[start] = word[end]
                word[end] = temp
                start += 1
                end -= 1
            elif word[start] not in vowels:
                start += 1
            else:
                end -= 1
        return ''.join(word)