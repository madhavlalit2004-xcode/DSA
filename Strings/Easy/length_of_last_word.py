# ============================================================
# LeetCode 58 - Length of Last Word
# ============================================================
# Given a string s consisting of words and spaces, return the
# length of the last word. A word is a maximal substring
# consisting of non-space characters.
#
# Example:
#   Input:  s = "Hello World"
#   Output: 5  ("World")
#
#   Input:  s = "   fly me   to   the moon  "
#   Output: 4  ("moon")
#
#   Input:  s = "luffy is still joyboy"
#   Output: 6  ("joyboy")
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — optimal approach
# ============================================================

#Approach 1: Scan from right to left (optimal)
def length_of_last_word_optimal(s):
    i = len(s) - 1

    while i >= 0 and s[i] == " ":
        i -= 1
    
    length = 0
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    return length