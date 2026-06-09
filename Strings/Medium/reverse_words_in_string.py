# ============================================================
# LeetCode 151 - Reverse Words in a String
# ============================================================
# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
#
# Return a string of the words in reverse order concatenated
# by a single space.
#
# Note:
# - Remove leading and trailing spaces
# - Reduce multiple spaces between words to a single space
#
# Example:
#   Input:  s = "the sky is blue"
#   Output: "blue is sky the"
#
#   Input:  s = "  hello world  "
#   Output: "world hello"
#
#   Input:  s = "a good   example"
#   Output: "example good a"
#
# Approach (Brute Force):
# - Use built-in split() to split words (automatically removes spaces)
# - Reverse the list of words
# - Join using single space
#
# Time Complexity:  O(n)
# Space Complexity: O(n)
#
# Approach (Optimal - Manual Parsing):
# - Traverse string character by character
# - Build words manually ignoring extra spaces
# - Store words in a list
# - Reverse the list
# - Join with single space
#
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================================

#Approach 1:
def reverse_words_optimal(s):
    words = []
    word = ""
    for char in s:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word = ""
            
    if word:
        words.append(word)
    
    return " ".join(words[::-1])