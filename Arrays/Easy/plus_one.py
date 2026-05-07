# ============================================================
# LeetCode 66 - Plus One
# ============================================================
# Given a large integer represented as an array of digits,
# increment the integer by one and return the resulting array.
# The digits are stored most-significant-digit first.
# No leading zeroes except for the number 0 itself.
#
# Example:
#   Input:  digits = [1, 2, 3]
#   Output: [1, 2, 4]  (123 + 1 = 124)
#
#   Input:  digits = [4, 3, 2, 1]
#   Output: [4, 3, 2, 2]  (4321 + 1 = 4322)
#
#   Input:  digits = [9]
#   Output: [1, 0]  (9 + 1 = 10)
#
#   Input:  digits = [9, 9, 9]
#   Output: [1, 0, 0, 0]  (999 + 1 = 1000)
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — in-place (except carry overflow case)
# ============================================================

#Approach 1: Brute Force (convert to int)
#Time: O(n)
def plus_one_brute(digits):
    num = int(''.join(map(str, digits)))
    return [int(d) for d in str(num + 1)]


#Approach 2: Traverse from right (optimal)
#Add 1 to last digit
#Time: O(n)
def plus_one_optimal(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits