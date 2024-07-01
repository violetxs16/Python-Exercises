#String practice one
#Implement an algorithm to check if a string has all unique characters

#Optimized Implementation
def unique_chars_2(test_str):
    dic = {}
    for i in range(len(test_str)):
        if test_str[i] in dic:
            return False
        else:
            dic[test_str[i]] = 0
    return True
def main():
    st = input("Input a String: ")
    print(unique_chars_2(st))
if __name__ == "__main__":
    main()
