# ============================================================
# LeetCode 2149 - Rearrange Array Elements by Sign
# ============================================================
# Given an array nums of even length with equal number of
# positive and negative integers, rearrange so that:
# - Every consecutive pair has opposite signs
# - Positives appear at even indices, negatives at odd indices
# - Relative order of positives and negatives is preserved
#
# Example:
#   Input:  nums = [3, 1, -2, -5, 2, -4]
#   Output: [3, -2, 1, -5, 2, -4]
#
#   Input:  nums = [-1, 1]
#   Output: [1, -1]
#
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================================

#Approach 1: Brute Force
#Time: O(n)
def rearrange_brute(nums):
    positive = []
    negative = []
    result = []
    for x in nums:
        if x > 0:
            positive.append(x)
        else:
            negative.append(x)
    for i in range(len(positive)):
        result.append(positive[i])
        result.append(negative[i])
    return result


#Approach 2: Two Pointer
#Place positive on even indices and negativeson odd indices
#Time: O(n)
def rearrange_two_pointers(nums):
    result = [0] * len(nums)
    pos = 0
    neg = 1
    for num in nums:
        if num > 0:
            result[pos] = num
            pos += 2
        else:
            result[neg] = num
            neg += 2
    return result