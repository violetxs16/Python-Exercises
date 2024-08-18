class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #Two pointer apprach: Starting from end and start
        #Continue until start < end or reach middle
        #Strings are immutable in python so must convert to list
        start = 0
        end = len(s) - 1
        while(start < end):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1

        