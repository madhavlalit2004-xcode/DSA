# ============================================================
# LeetCode 560 - Subarray Sum Equals K
# ============================================================
# Given an array of integers nums and an integer k, return
# the total number of subarrays whose sum equals k.
#
# Example:
#   Input:  nums = [1, 1, 1], k = 2
#   Output: 2
#
#   Input:  nums = [1, 2, 3], k = 3
#   Output: 2  ([1,2] and [3])
#
#   Input:  nums = [1, -1, 1], k = 1
#   Output: 3
#
# Time Complexity:  O(n)   — Prefix Sum + HashMap
# Space Complexity: O(n)
# ============================================================

#Approach 1: Brute Force
#Time: O(n^2)
def subarray_sum_brute(nums, k):
    count = 0
    for i in range(nums):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                count += 1
    return count


#Approach 2: Prefix Sum + Hashmap
#prefix_sum = sum of nums[0...i]
#if prefix_sum[j] - prefix_sum[i] == k
#the subarray [i+1, j] has sum k
#Time: O(n)
def subarray_sum_optimal(nums, k):
    count = 0
    prefix_sum = 0
    freq = {0:1}

    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in freq:
            count += freq[prefix_sum - k]
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    return count