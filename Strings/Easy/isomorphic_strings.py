# ============================================================
# LeetCode 205 - Isomorphic Strings
# ============================================================
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if characters in s can be replaced
# to get t, with the following rules:
#   - All occurrences of a character must be replaced with the same character
#   - No two characters may map to the same character
#   - A character may map to itself
#
# Example:
#   Input:  s = "egg", t = "add"
#   Output: True   (e→a, g→d)
#
#   Input:  s = "foo", t = "bar"
#   Output: False  (o→a and o→r — contradiction)
#
#   Input:  s = "paper", t = "title"
#   Output: True   (p→t, a→i, e→e, r→r)
#
#   Input:  s = "badc", t = "baba"
#   Output: False  (a→b and c→b — two chars map to same)
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — at most 256 unique characters
# ============================================================

#Approach 1: Two Hashmaps
def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False
    
    freq1 = {}
    freq2 = {}

    for i in range(len(s)):
        if s[i] in freq1 and freq1[s[i]] != t[i]:
            return False
        if t[i] in freq2 and freq2[t[i]] != s[i]:
            return False
        
        freq1[s[i]] = t[i]
        freq2[t[i]] = s[i]

    return True