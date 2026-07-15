# ============================================================
# LeetCode 680 - Valid Palindrome II
# ============================================================
# Given a string s, return True if s can be a palindrome
# after deleting at most ONE character.
#
# Example:
#   Input:  s = "aba"
#   Output: True   (already a palindrome)
#
#   Input:  s = "abca"
#   Output: True   (delete 'c' or 'b' → "aba" or "aca")
#
#   Input:  s = "abc"
#   Output: False  (can't make palindrome with one deletion)
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Two Pointer (optimal)
def is_palindrome(s, left, right):
    while left < right:
        if s[left] < s[right]:
            return False
        left += 1
        right -= 1
    return True

def valid_palindrome_optimal(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] < s[right]:
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True