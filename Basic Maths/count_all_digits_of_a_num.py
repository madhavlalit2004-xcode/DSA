# ============================================================
# Count All Digits of a Number
# ============================================================
# Given an integer n, return the number of digits in it.
#
# Example:
#   Input:  n = 12345
#   Output: 5
#
#   Input:  n = 7
#   Output: 1
#
# Time Complexity:  O(log10(n))
# Space Complexity: O(1)
# ============================================================

#Approach 1: Loop
def count_digits(num):
    num = abs(num)
    if num == 0:
        return 1
    
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count


#Approach 2: String Conversion
def count_digit(num):
    return len(str(abs(num)))