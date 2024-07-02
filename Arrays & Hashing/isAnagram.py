#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#Easy
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #Case 1: lengths are different
            return False
        str1_chars = {}
        str2_chars = {}
        for i in range(len(s)):
            str1_chars[s[i]] = 1 + str1_chars.get(s[i],0)#Get key, return 0 if key not found
            str2_chars[t[i]] = 1 + str2_chars.get(t[i],0)
        return str1_chars == str2_chars