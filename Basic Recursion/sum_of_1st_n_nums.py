# ============================================================
# Sum of First N Numbers Using Recursion
# ============================================================
# Given a number n, return the sum of all numbers from 1 to n
# using recursion — without any loops.
#
# Example:
#   Input:  n = 5
#   Output: 15  (1 + 2 + 3 + 4 + 5)
#
#   Input:  n = 10
#   Output: 55
#
# Time Complexity:  O(n)  — n recursive calls
# Space Complexity: O(n)  — n frames on the call stack
# ============================================================

#Approach1: Functional Recursion
def sum(num):
    if num == 0:
        return 0
    return num + sum(num-1)