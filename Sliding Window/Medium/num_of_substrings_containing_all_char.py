# ============================================================
# LeetCode 1358 - Number of Substrings Containing All Three Characters
# ============================================================
# Given a string s consisting only of characters a, b, c,
# return the number of substrings that contain at least one
# occurrence of all three characters.
#
# Example:
#   Input:  s = "abcabc"
#   Output: 10
#
#   Input:  s = "aaacb"
#   Output: 3
#
#   Input:  s = "abc"
#   Output: 1
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — fixed size frequency map (3 chars)
# ============================================================

#Approach 1: Brute Force
def count_substring_brute(s):
    count = 0
    n = len(s)

    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(s[j])
            if len(seen) == 3:
                count += (n-j)
                break
    return count


#Approach 2: Sliding Window (optimal)
def count_substring_optimal(s):
    count = 0
    n = len(s)
    freq = {}
    left = 0

    for right in range(n):
        freq[s[right]] += 1

        while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
            count += len(s) - right
            freq[s[left]] -= 1
    return count