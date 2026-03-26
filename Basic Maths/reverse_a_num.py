# ============================================================
# Reverse a Number
# ============================================================
# Given an integer n, return its reverse.
# If the reversed number overflows, return 0.
#
# Example:
#   Input:  n = 12345
#   Output: 54321
#
#   Input:  n = -456
#   Output: -654
#
#   Input:  n = 1200
#   Output: 21
#
# Time Complexity:  O(log(n))
# Space Complexity: O(1)
# ============================================================

#Approach 1: Loop
def reverse_nums1(num):
    negative = num < 0
    num = abs(num)
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reverse_num = reverse_num*10 + digit
        num //= 10
    return -reversed_num if negative else reverse_num


#Approach 2: String Conversion
def reverse_nums2(num):
    negative = num < 0
    reverse_num = int(str(abs(num))[::-1])
    return -reverse_num if negative else reverse_num