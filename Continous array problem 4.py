#Given a string s, find the longest continous substring with no more than k distinct characters
#approach: sliding window approach
#Use: dictionary

def k_distinct_chars(str , k):
    distinct_chars = {}
    # We will add the characters to the dictionary & increase values if duplicates are found
    distinct_substr = ""
    start_distinct = 0
    end_distinct = 0
    index_start = 0
    num_distinct = 0
    #Step 1: Iterate through all characters of str
    #Step 2: Append to the distinct_substr & character to dictionary
    #           ---we access str[index_start] to remove char from dictionary
    #Step 3: Check if length of dictionary is greater than k: means we have more than k chars
    #We need to check dictionary values to see number of distinct characters in current substring
    #We need to record highest value & compare to new dictionary value when char gets inserted
    #if value is greater we update start_distinct & end_distinct values
    for i in range(len(str)):
        if str[i] not in distinct_chars:
            distinct_chars[str[i]] = 1 #Add new char
        else:
            distinct_chars[str[i]] += 1 #Increase value

        distinct_substr += str[i]
        if len(distinct_chars) > k:
            distinct_chars[str[index_start]] -= 1 #Decrease char value
            distinct_substr = distinct_substr[1:] #Cut out first char
            index_start += 1
            total_unique = 0
            for val in distinct_chars.values():
                total_unique += val 
            if total_unique > num_distinct:#There is more unique characters in current dictionary
                #Keep track of str longest substring
                start_distinct = index_start
                end_distinct = i
                num_distinct = total_unique
    
    return str[start_distinct:end_distinct+1]
str1 = "Umbrella"
print(k_distinct_chars(str1, 2))
str2 = "hello"
print(k_distinct_chars(str2, 3))