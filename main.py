# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    checkList = []
    for alpha in word:
        #print(alpha + str(word.count(alpha)) + str(anagram.count(alpha)))
        if word.count(alpha) == anagram.count(alpha):
            checkList.append(True)
        else:
            checkList.append(False)
    #print(checkList)
    return  False not in checkList

print(find_anagrams('below','elbow'))

