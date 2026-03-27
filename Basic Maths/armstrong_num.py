# ============================================================
# Armstrong Number
# ============================================================
# A number is an Armstrong number if the sum of its digits
# each raised to the power of the number of digits equals
# the number itself.
#
# Example:
#   Input:  n = 153
#   Output: True   (1³ + 5³ + 3³ = 1 + 125 + 27 = 153)
#
#   Input:  n = 9474
#   Output: True   (9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561+256+2401+256 = 9474)
#
#   Input:  n = 123
#   Output: False  (1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123)
#
# Time Complexity:  O(log10(n))
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force ( stru=ing to digits)
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num


#Approach 2: Loop
def armstrong(num):
    total = 0
    orignal = num
    while num > 0:
        digit = num % 10
        total += digit ** len(str(num))
        num //= 10
    return total == orignal