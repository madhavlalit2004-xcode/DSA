# ============================================================
# LeetCode 509 - Fibonacci Number
# ============================================================
# The Fibonacci sequence: F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2) for n > 1
#
# Example:
#   Input:  n = 5
#   Output: 5   (0 1 1 2 3 5)
#
#   Input:  n = 10
#   Output: 55
#
#   Input:  n = 0
#   Output: 0
#
# ============================================================

#Approach 1: Recursion
#Time: O(2^n)
def fib_recursion(num):
    if num <= 1:
        return num
    return fib_recursion(num-1) + fib_recursion(num-2)