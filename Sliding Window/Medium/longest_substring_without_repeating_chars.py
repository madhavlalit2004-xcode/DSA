# ============================================================
# LeetCode 3 - Longest Substring Without Repeating Characters
# ============================================================
# Given a string s, find the length of the longest substring
# without repeating characters.
#
# Example:
#   Input:  s = "abcabcbb"
#   Output: 3   ("abc")
#
#   Input:  s = "bbbbb"
#   Output: 1   ("b")
#
#   Input:  s = "pwwkew"
#   Output: 3   ("wke")
#
# Time Complexity:  O(n)   — Sliding Window
# Space Complexity: O(min(n, 26))  — at most 26 unique chars
# ============================================================

#Approach 1: Bruete force
def longest_substring_brute(s):
    max_len = 0
    n = len(s)
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len


#Approach 2: Sliding Window (optimal)
def longest_substring_optimal(s):
    last_seen = {}
    left = 0
    ans = 0

    for right in range(len(s)):
        if s[right] in last_seen:
            left = max(left, last_seen[s[right]] + 1)
        
        last_seen[s[right]] = right
        ans = max(ans, right - left + 1)

    return ans