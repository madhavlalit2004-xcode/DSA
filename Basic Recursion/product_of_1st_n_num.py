# ============================================================
# Product of First N Numbers Using Recursion
# ============================================================
# Given a number n, return the product of all numbers from
# 1 to n using recursion — without any loops.
# Note: This is the same as finding the Factorial of n.
#
# Example:
#   Input:  n = 5
#   Output: 120  (1 * 2 * 3 * 4 * 5)
#
#   Input:  n = 6
#   Output: 720
#
#   Input:  n = 0
#   Output: 1   (0! = 1 by definition)
#
# Time Complexity:  O(n)  — n recursive calls
# Space Complexity: O(n)  — n frames on the call stack
# ============================================================

#Approach 1: Functional Recursion
def product(nums):
    if nums == 0:
        return 1
    return nums * product(nums - 1)