# ============================================================
# Leetcoe - 7
# ============================================================
# Given a signed 32-bit integer x, return x with its digits
# reversed.
#
# If reversing x causes the value to go outside the signed
# 32-bit integer range [-2^31, 2^31 - 1], return 0.
#
# You must not use 64-bit integers.
#
# Must run in O(log n) time and O(1) space.
#
# Example:
#   Input:  x = 123
#   Output: 321
#
#   Input:  x = -123
#   Output: -321
#
#   Input:  x = 120
#   Output: 21
#
# Key Insight:
#   Extract last digit using:
#       digit = x % 10
#
#   Build reversed number using:
#       rev = rev * 10 + digit
#
#   Before updating rev, check for 32-bit overflow.
#
#   If rev exceeds integer range:
#       → return 0
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approacch 1: optimal
def reverse_integer(x):
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1

    ans = 0
    sign = 1

    if x < 0:
        sign = -1
        x = -x
    while (x > 0):
        n = x % 10
        ans = ans * 10 + n
        x //= 10

    ans *= sign
    if ans < INT_MIN or ans > INT_MAX:
        return 0
    return ans