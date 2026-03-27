# ============================================================
# Print All Divisors of a Number
# ============================================================
# Given an integer n, print all numbers that divide n
# completely (i.e. leave no remainder).
#
# Example:
#   Input:  n = 36
#   Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
#
#   Input:  n = 12
#   Output: [1, 2, 3, 4, 6, 12]
#
#   Input:  n = 7
#   Output: [1, 7]   (prime number — only 2 divisors)
#
# Time Complexity:  O(sqrt(n))  — optimal approach
# Space Complexity: O(d)        — d = number of divisors
# ============================================================

#Approach 1: Brute Force(check every num up to n)
#Time: O(n)
def divisors_brute(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


#Approach 2: Optimal(loop only upto sqrt(n))
#Time: O(sqrt(n))
import math

def divisor_optimal(num):
    divisors = []
    for i in range(1, math.sqrt(num) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num//i)
    return sorted(divisors)