# ============================================================
# Palindrome Number
# ============================================================
# Given an integer n, return True if it is a palindrome,
# False otherwise.
# A number is a palindrome if it reads the same forwards
# and backwards.
#
# Example:
#   Input:  n = 121
#   Output: True
#
#   Input:  n = -121
#   Output: False  (negative numbers are not palindromes)
#
#   Input:  n = 1221
#   Output: True
#
#   Input:  n = 10
#   Output: False
#
# Time Complexity:  O(log10(n))
# Space Complexity: O(1)
# ============================================================

#Approach 1: Reverse the full num and Compare
def is_palindrome(num):
    if num < 0:
        return False
    
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num*10 + digit
        n //= 10
    return num == reversed_num


#Approach 2: String Conversion
def is__palindrome(num):
    if num < 0:
        return False
    s = str(num)
    return s == s[::-1]