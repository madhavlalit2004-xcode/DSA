# ============================================================
# LeetCode 151 - Reverse Words in a String
# ============================================================
# Given a string s, reverse the order of the words.
# A word is a sequence of non-space characters.
# Words are separated by at least one space.
# Return a single space-separated string with words in reverse.
# Leading/trailing spaces and extra spaces between words
# must be removed.
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
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================================

#Approach 1: Build in split and join
#Time: O(n)
def rev_words(s):
    return ' '.join(s.split()[::-1])


#Approach 2: Two Pointer
def reverse_words(s):
    result = []
    word = ""

    for char in s:
        if char != " ":
            word += char
        else:
            if word:
                result.append(word)
                word = ""
    
    if word:
        result.append(word)