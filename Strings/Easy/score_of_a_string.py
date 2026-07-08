# ============================================================
# LeetCode 3110 - Score of a String
# ============================================================
# Given a string s, return the score of s which is defined as
# the sum of the absolute differences of adjacent characters.
# Absolute difference = |ord(s[i]) - ord(s[i+1])|
#
# Example:
#   Input:  s = "hello"
#   Output: 13
#   Explanation:
#     |h-e| = |104-101| = 3
#     |e-l| = |101-108| = 7
#     |l-l| = |108-108| = 0
#     |l-o| = |108-111| = 3
#     Total = 3 + 7 + 0 + 3 = 13
#
#   Input:  s = "zaz"
#   Output: 50
#   Explanation:
#     |z-a| = |122-97| = 25
#     |a-z| = |97-122| = 25
#     Total = 50
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: 
def score_linier(s):
    score = 0
    for i in range(len(s) - 1):
        score += abs(ord(s[i]) - ord(s[i+1]))
    return score