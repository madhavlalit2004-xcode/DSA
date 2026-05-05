# ============================================================
# LeetCode 5 - Longest Palindromic Substring
# ============================================================
# Given a string s, return the longest palindromic substring.
#
# Example:
#   Input:  s = "babad"
#   Output: "bab" or "aba"  (both valid)
#
#   Input:  s = "cbbd"
#   Output: "bb"
#
#   Input:  s = "a"
#   Output: "a"
#
#   Input:  s = "racecar"
#   Output: "racecar"
#
# Time Complexity:  O(n^2)  — Expand Around Center
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force
#Time: O(n^3)
def longest_palindrome_brute(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    result = s[0]
    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            sub = s[i:j]
            if is_palindrome(sub) and len(sub) > len(result):
                result = sub
    return result


#Approach 2:Expand around centre
#Time: O(n^2)
def longest_palindrome_expand(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
    
    result = ""
    for i in range(len(s)):
        odd  = expand(i, i)           
        even = expand(i, i + 1)     
        if len(odd)  > len(result): result = odd
        if len(even) > len(result): result = even
 
    return result