# ============================================================
# GCD of Two Numbers
# ============================================================
# Given two integers a and b, return their Greatest Common
# Divisor (GCD) — the largest number that divides both.
#
# Example:
#   Input:  a = 12, b = 8
#   Output: 4
#
#   Input:  a = 100, b = 75
#   Output: 25
#
#   Input:  a = 7, b = 5
#   Output: 1
#
# Time Complexity:  O(log(min(a, b)))  — Euclidean Algorithm
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Froce(check all divisors up yo min(a, b))
def gcd_brute(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


#Approach 2: Euclidean Algorithm
def gcd_optimal(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    return a