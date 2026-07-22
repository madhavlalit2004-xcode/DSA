# ============================================================
# LeetCode 643 - Maximum Average Subarray I
# ============================================================
# Given an integer array nums and integer k, find the contiguous
# subarray of length k that has the maximum average value.
# Return the maximum average.
#
# Example:
#   Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
#   Output: 12.75  (subarray [12, -5, -6, 50] → avg = 51/4 = 12.75)
#
#   Input:  nums = [5], k = 1
#   Output: 5.0
#
# Time Complexity:  O(n)   — Sliding Window
# Space Complexity: O(1)
# ============================================================

#Approach 1: Sliding Window (optimal)
def max_avg_subbaray_optimal(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i-k]

        max_sum = max(max_sum, window_sum)
    
    return max_sum / float(k)