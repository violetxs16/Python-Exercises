#Given a string s, find the longest continous substring with no more than k distinct characters
#approach: sliding window approach
#Use: dictionary

def k_distinct_chars(str_1 , k):
    distinct_chars = {}
    # We will add the characters to the dictionary & increase values if duplicates are found
    distinct_substr = ""
    greatest_distinct_subtr = ""
    index_start = 0
    #Step 1: Iterate through all characters of str
    #Step 2: Append to the distinct_substr & character to dictionary
    #           ---we access str[index_start] to remove char from dictionary
    #Step 3: Check if length of dictionary is greater than k: means we have more than k chars
    #We need to check dictionary values to see number of distinct characters in current substring
    #We need to record highest value & compare to new dictionary value when char gets inserted
    #if value is greater we update start_distinct & end_distinct values
    for i in range(len(str_1)):
        if str_1[i] not in distinct_chars:
            distinct_chars[str_1[i]] = 1 #Add new char
        else:
            distinct_chars[str_1[i]] += 1 #Increase value

        distinct_substr += str_1[i] #Append char to substr
       
        while(len(distinct_chars) > k ): #Keep decreasing number of chars until we have k number
            distinct_chars[str_1[index_start]] -= 1
            distinct_substr = distinct_substr[1:]
            if distinct_chars[str_1[index_start]] == 0: #Delete key with value zero
                del distinct_chars[str_1[index_start]]
            index_start += 1
        

        if len(distinct_substr) > len(greatest_distinct_subtr):
            greatest_distinct_subtr = distinct_substr

    
    return greatest_distinct_subtr
str1 = "cbbebi"
print(k_distinct_chars(str1, 3))
str2 = "hello"
print(k_distinct_chars(str2, 3))