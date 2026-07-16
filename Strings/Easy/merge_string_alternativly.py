# ============================================================
# LeetCode 1768 - Merge Strings Alternately
# ============================================================
# Given two strings word1 and word2, merge them alternately.
# Append the extra characters of the longer string at the end.
#
# Example:
#   Input:  word1 = "abc", word2 = "pqr"
#   Output: "apbqcr"
#
#   Input:  word1 = "ab", word2 = "pqrs"
#   Output: "apbqrs"   (extra "rs" appended)
#
#   Input:  word1 = "abcd", word2 = "pq"
#   Output: "apbqcd"   (extra "cd" appended)
#
# Time Complexity:  O(m + n)
# Space Complexity: O(m + n)
# ============================================================


#Approach 1: Two Pointer (optimal)
def merge_string_alter_optimal(word1, word2):
    result = []
    i = 0
    j = 0

    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1
    
    while i < len(word1):
        result.append(word1[i])
        i += 1
    
    while j < len(word2):
        result.append(word2[j])
        j += 1
    
    return "".join(result)