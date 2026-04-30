# ============================================================
# LeetCode 242 - Valid Anagram
# ============================================================
# Given two strings s and t, return True if t is an anagram
# of s, and False otherwise.
# An anagram uses all original letters exactly once.
#
# Example:
#   Input:  s = "anagram", t = "nagaram"
#   Output: True
#
#   Input:  s = "rat", t = "car"
#   Output: False
#
#   Input:  s = "a", t = "a"
#   Output: True
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — at most 26 letters
# ============================================================

#Approach 1: Frequency Count using Array(optimal)
#Time: O(n)
def valid_anagrams_optimal(s, t):
    if len(s) != len(t):
        return False

    freq1 = {}
    for i in s:
        freq1[i] = freq1.get(i, 0) + 1

    freq2 = {}
    for i in s:
        freq2[i] = freq2.get(i, 0) + 1
    
    if freq1 == freq2 :
        return True
    else:
        return False