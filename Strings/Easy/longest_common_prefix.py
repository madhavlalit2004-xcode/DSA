# ============================================================
# LeetCode 14 - Longest Common Prefix
# ============================================================
# Given an array of strings 'strs', return the longest common
# prefix among all the strings.
#
# If there is no common prefix, return an empty string "".
#
# Example:
#   Input:
#       strs = ["flower", "flow", "flight"]
#   Output:
#       "fl"
#
#   Explanation:
#       Common prefixes:
#       "f"  ✓
#       "fl" ✓
#       "flo" ✗ (because "flight" does not have "flo")
#
# ------------------------------------------------------------
#
# Example:
#   Input:
#       strs = ["dog", "racecar", "car"]
#   Output:
#       ""
#
#   Explanation:
#       There is no common prefix among all strings.
#
# ------------------------------------------------------------
#
# Key Insight:
#   Compare characters at the same index in every string.
#
#   - Take the first string as the reference.
#   - For each character in the first string:
#       * Compare it with the character at the same position
#         in every other string.
#       * If any string ends or characters differ,
#         return the prefix collected so far.
#   - If all characters match, continue.
#
# Time Complexity:
#   O(n × m)
#
#   where:
#       n = number of strings
#       m = length of the shortest string
#
# Space Complexity:
#   O(1)
#   (excluding the output string)
# ============================================================

#Approach 1: Optimal (sort)
def longest_common_prefix(strs):
    strs.sort()
    first = strs[0]
    last = strs[-1]
    result = ""

    for i in len(strs):
        if first[i] != last[i]:
            break
        result += first[i]
    return result