# ============================================================
# LeetCode 238 - Product of Array Except Self
# ============================================================
# Given an integer array nums, return an array answer such that
# answer[i] is the product of all elements except nums[i].
# Must run in O(n) time without using division.
#
# Example:
#   Input:  nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
#
#   Input:  nums = [-1, 1, 0, -3, 3]
#   Output: [0, 0, 9, 0, 0]
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — optimal (output array not counted)
# ============================================================

#Approach 1: Brute Force
def product_except_self(nums):
    n = len(nums)
    result = []

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    return result


#Approach 2: Prefix and Suffix array(optimal)
def product_except_self_optimal(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i -1] * n[i - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    
    return [prefix[i] * suffix[i] for i in range(n)]