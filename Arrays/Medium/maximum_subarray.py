# ============================================================
# LeetCode 53 - Maximum Subarray
# ============================================================
# Given an integer array nums, find the subarray with the
# largest sum and return its sum.
#
# Example:
#   Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#   Output: 6  (subarray [4, -1, 2, 1])
#
#   Input:  nums = [1]
#   Output: 1
#
#   Input:  nums = [5, 4, -1, 7, 8]
#   Output: 23
#
# Time Complexity:  O(n)   — Kadane's Algorithm
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force 
#Check every subarray and track the max sum
#Time: O(n^2)
def max_subbaray_brute(nums):
    max_sum = float('-inf')
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            max_sum = max(total, max_sum)
    return max_sum


#Approach 2: Kadane's Algorithm (optimal)
#Time: O(n)
def maximum_subarray_optimal(nums):
    max_sum = float(-'inf')
    curr_sum = 0
    for num in nums:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum