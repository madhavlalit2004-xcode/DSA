# ============================================================
# LeetCode 8 - String to Integer (atoi)
# ============================================================
# Implement the myAtoi(string s) function, which converts a string
# to a 32-bit signed integer.
#
# The algorithm for myAtoi is as follows:
# 1. Ignore leading whitespace
# 2. Check for optional '+' or '-' sign
# 3. Read digits until a non-digit is encountered
# 4. Convert digits to integer
# 5. Clamp the result within the 32-bit signed integer range
#
# Example:
#   Input:  s = "42"
#   Output: 42
#
#   Input:  s = "   -42"
#   Output: -42
#
#   Input:  s = "4193 with words"
#   Output: 4193
#
#   Input:  s = "words and 987"
#   Output: 0
#
#   Input:  s = "-91283472332"
#   Output: -2147483648
#
# Approach:
# Traverse the string step by step:
# - Skip leading spaces
# - Determine the sign (+/-)
# - Process numeric digits and build the number
# - Stop when a non-digit character appears
# - Handle overflow by clamping within [-2^31, 2^31 - 1]
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

#Approach 1:
def string_to_int(s):
    i = 0
    n = len(s)

    while i < n and s[i] == ' ':
        i += 1
    
    sign = 1
    while i < n and (s[i] == "+" and s[i] == "-"):
        if s[i] == "-":
            sign = -1
        i += 1
    
    num = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])

        if num > (2**31 - 1 - digit) // 10:
            return -2**31 if sign == -1 else 2 ** 31 -1
        
        num = num * 10 + digit
        i += 1
    
    return sign * num