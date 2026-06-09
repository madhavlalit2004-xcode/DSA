# ============================================================
# LeetCode 1781 - Sum of Beauty of All Substrings
# ============================================================
# The beauty of a string is defined as the difference between the
# frequency of the most frequent character and the least frequent
# character (excluding characters with 0 frequency).
#
# Given a string s, return the sum of beauty of all its substrings.
#
# Example:
#   Input:  s = "aabcb"
#   Output: 5
#   Explanation:
#   Substrings like "aab", "aabc", "abcb", etc. contribute to beauty.
#
#   Input:  s = "aabcbaa"
#   Output: 17
#
# Approach (Brute Force):
# - Generate all substrings
# - For each substring, count frequency using dictionary
# - Compute max and min frequency
# - Add (max - min) to result
#
# Time Complexity:  O(n^3)
# Space Complexity: O(1)
#
# Approach (Optimal):
# - Fix starting index i
# - Use a frequency array (size 26)
# - Expand substring to the right
# - Update frequency dynamically
# - At each step compute max and min frequency
#
# Time Complexity:  O(n^2 * 26) ≈ O(n^2)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force
def beauty_of_substrings_brute(s):
    n = len(s)
    total = 0

    for i in range(n):
        for j in range(i, n):
            freq = {}
            for k in range(i, j+1):
                if s[k] in freq:
                    freq[s[k]] += 1
                else:
                    freq[s[k]] = 1
            
            values = freq.values()
            total += max(values) - min(values)
    return total