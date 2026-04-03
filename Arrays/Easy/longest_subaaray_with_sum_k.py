# ============================================================
# Longest Subarray with Given Sum K
# ============================================================
# Given an array nums and an integer k, return the length of
# the longest subarray whose elements sum to k.
#
# Example:
#   Input:  nums = [1, 2, 3, 1, 1, 1, 1], k = 3
#   Output: 4  ([1, 1, 1, 1] or [3] but [1,1,1,1] is longer)
#
#   Input:  nums = [1, -1, 5, -2, 3], k = 3
#   Output: 4  ([1, -1, 5, -2])
#
#   Input:  nums = [-2, -1, 2, 1], k = 1
#   Output: 2  ([-1, 2])
#
# ============================================================

#Approach 1: Brute Force
#Time: O(n^2)
def longest_subarray_brute(nums, k):
    max_len = 0
    for i in range(len(nums)):
        total = 0
        for j in range(1, len(nums)):
            total += nums[j]
            if total == k:
                max_len = max(max_len, j - i + 1)
    return max_len


#Approach 2: Two Pointer
#Time: O(n)
def longest_subarray_sliding_window(nums, k):
    left = 0
    total = 0
    max_len = 0

    for right in range(len(nums)):
        total += nums[right]

        while total > k and left <= right:
            total -= nums[left]
            left += 1
        
        if total == k:
            max_len = max(max_len, right - left + 1)
    
    return max_len