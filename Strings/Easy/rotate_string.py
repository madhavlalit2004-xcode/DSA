# ============================================================
# LeetCode 796 - Rotate String
# ============================================================
# Given two strings s and goal, return True if s can become
# goal after some number of shifts.
# A shift moves the leftmost character to the rightmost position.
#
# Example:
#   Input:  s = "abcde", goal = "cdeab"
#   Output: True   (shift 2 times: abcde → bcdea → cdeab)
#
#   Input:  s = "abcde", goal = "abced"
#   Output: False
#
#   Input:  s = "aa", goal = "aa"
#   Output: True   (0 shifts)
#
# Key Insight:
#   If we double s → s+s, then every possible rotation of s
#   appears as a substring of s+s.
#
# Time Complexity:  O(n)   — KMP / built-in 'in'
# Space Complexity: O(n)
# ============================================================

#Approach 1: Brute Force
#Time:(On^2)
def rotate_string_brute(s, goal):
    if len(s) != len(goal):
        return False
    n = len(s)
    for i in range(n):
        if s[i:] + s[:i] == goal:
            return True
        return False
    

#Approach 2: Double string (optimal):
#s + s contains all rotations of s as substring
#Time: O(n)
def rotate_string_optimal(s, goal):
    if len(s) != len(goal):
        return False
    if goal in (s+s):
        return True
    else:
        return False