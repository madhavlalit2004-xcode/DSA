# ============================================================
# LeetCode 1903 - Largest Odd Number in String
# ============================================================
# Given a string num representing a large integer,
# return the largest-valued odd integer that is a non-empty
# prefix of num, or "" if no odd integer exists.
#
# A prefix is the beginning portion of the string.
#
# Example:
#   Input:  num = "52"
#   Output: "5"   (5 is odd, 52 is even)
#
#   Input:  num = "4206"
#   Output: ""    (no odd prefix exists)
#
#   Input:  num = "35427"
#   Output: "35427"  (entire number is odd)
#
# Key Insight:
#   A number is odd if its LAST digit is odd.
#   So scan from right to left for the first odd digit.
#   Return everything from start up to and including that digit.
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Right to left Scan
def largets_odd_sum(num):
    for i in range(len(num) - 1, -1, -1):
        if num[i] in "13579":
            return num[:i+1]
    return ""