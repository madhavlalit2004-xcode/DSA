# ============================================================
# LeetCode 451 - Sort Characters by Frequency
# ============================================================
# Given a string s, sort it in decreasing order based on the
# frequency of the characters. Return the sorted string.
# If there are multiple answers, return any of them.
#
# Example:
#   Input:  s = "tree"
#   Output: "eert"  (e appears twice, t and r appear once)
#
#   Input:  s = "cccaaa"
#   Output: "aaaccc" or "cccaaa"  (both valid)
#
#   Input:  s = "Aabb"
#   Output: "bbAa" or "bbaA"  ('A' and 'a' are different)
#
# Time Complexity:  O(n log n)  — sorting dominates
# Space Complexity: O(n)
# ============================================================

#Approach 1: Brute Force (sort charchters directly)
#Time: O(n log n)
def freq_sort_brute(s):
    freq = []
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    return ''.join(sorted(s, key= lambda ch: -freq[ch]))


#Approach 1: Optimal (Hashmap + sorting)
#Time: O(n log n)
def freq_sort_optimal(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    sorted_chars = sorted(freq, key = lambda ch: -freq[ch])
    return ''.join(ch * freq[ch] for ch in sorted_chars)