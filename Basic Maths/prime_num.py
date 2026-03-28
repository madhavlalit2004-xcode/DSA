# ============================================================
# Check for Prime Number
# ============================================================
# A number is prime if it is greater than 1 and has no
# divisors other than 1 and itself.
#
# Example:
#   Input:  n = 7
#   Output: True   (divisors: 1, 7 only)
#
#   Input:  n = 12
#   Output: False  (divisors: 1, 2, 3, 4, 6, 12)
#
#   Input:  n = 1
#   Output: False  (1 is not prime by definition)
#
# Time Complexity:  O(sqrt(n))  — optimal approach
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force(check all nums from 2 to n-1)
#Time: O(n)
def prime_brute(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


#Approach 2: Optimal (check uptio sqrt(num))
#Time: O(sqrt(n))
import math

def prime_optimal(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True