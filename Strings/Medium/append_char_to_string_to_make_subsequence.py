# ============================================================
# LeetCode 2486 - Append Characters to String to Make Subsequence
# ============================================================
# Given two strings s and t, return the minimum number of
# characters that need to be appended to the END of s so
# that t becomes a subsequence of s.
#
# Example:
#   Input:  s = "coaching", t = "coding"
#   Output: 4
#   Explanation: Match "co_i_" → "c","o" matched, need to append "ding"
#                → append 4 characters
#
#   Input:  s = "abcde", t = "a"
#   Output: 0   (t is already a subsequence of s)
#
#   Input:  s = "z", t = "abcde"
#   Output: 5   (none matched, append all 5 chars of t)
#
# Key Insight:
#   Find how many characters of t are already a subsequence of s
#   The answer = len(t) - (matched characters)
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Two Pointer (optimal)
def append_char_optimal(s, t):
    i = 0
    j = 0
    while i < len(t) and j < len(s):
        if t[i] == s[j]:
            i += 1
        j += 1
    return len(t) - i