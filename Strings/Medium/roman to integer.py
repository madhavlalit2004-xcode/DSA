# ============================================================
# :contentReference[oaicite:1]{index=1}
# ============================================================
# Given a roman numeral, convert it to an integer.
#
# Roman numerals are represented by:
#   I = 1, V = 5, X = 10, L = 50,
#   C = 100, D = 500, M = 1000
#
# Usually, symbols are added.
# But in some cases, a smaller value before a larger value
# means subtraction.
#
# Must run in O(n) time and O(1) space.
#
# Example:
#   Input:  s = "III"
#   Output: 3
#
#   Input:  s = "LVIII"
#   Output: 58   (L=50, V=5, III=3)
#
#   Input:  s = "MCMXCIV"
#   Output: 1994 (M=1000, CM=900, XC=90, IV=4)
#
# Key Insight:
#   If current value < next value → subtract it
#   Else → add it
#
#   This handles all special cases like IV, IX, XL, etc.
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

#Approach 1:
def roman_to_numerical(s):
    roman = {
            'I': 1, 'V': 5, 'X': 10, 
            'L': 50, 'C': 100, 
            'D': 500, 'M': 1000
        }

    total = 0
    
    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total