# ============================================================
# LeetCode 125 - Valid Palindrome
# ============================================================
# A phrase is a palindrome if, after converting all uppercase
# letters to lowercase and removing all non-alphanumeric
# characters, it reads the same forward and backward.
#
# Example:
#   Input:  s = "A man, a plan, a canal: Panama"
#   Output: True
#
#   Input:  s = "race a car"
#   Output: False
#
#   Input:  s = " "
#   Output: True
#
# ============================================================

#Approach 1: Two Pointers
#Time: O(n)
def is_palindrome(str, left, right):
    if left >= right:
        return True
    if str[left].lower() != str[right].lower():
        return False
    return is_palindrome(str, left + 1, right - 1)