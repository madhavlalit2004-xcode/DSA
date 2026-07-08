# ============================================================
# LeetCode 392 - Is Subsequence
# ============================================================
# Given two strings s and t, return True if s is a subsequence
# of t, False otherwise.
# A subsequence is formed by deleting some characters from t
# without changing the relative order of the remaining characters.
#
# Example:
#   Input:  s = "ace", t = "abcde"
#   Output: True   (a_c_e found in abcde)
#
#   Input:  s = "aec", t = "abcde"
#   Output: False  (order matters: e comes before c in s but not in t)
#
#   Input:  s = "", t = "ahbgdc"
#   Output: True   (empty string is subsequence of anything)
#
# Time Complexity:  O(n)   — Two Pointer
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force (recursion)
def is_subsequence_brute(s, t, i = 0, j = 0):
    if i == len(s):
        return True
    if j == len(t):
        return False
    if s[i] == t[j]:
        return is_subsequence_brute(s, t, i+1, j+1)
    return is_subsequence_brute(s, t, i, j+1)


#Approach 2: Two Pointer (optimal)
def is_subsequence_optimal(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)