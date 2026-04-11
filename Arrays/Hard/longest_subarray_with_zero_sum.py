# ============================================================
# Length of Longest Subarray with Zero Sum
# ============================================================
# Given an array nums, find the length of the longest
# subarray whose elements sum to 0.
#
# Example:
#   Input:  nums = [15, -2, 2, -8, 1, 7, 10, 23]
#   Output: 5  (subarray [-2, 2, -8, 1, 7])
#
#   Input:  nums = [1, 0, -4, 3, 1, 0]
#   Output: 5  ([0, -4, 3, 1, 0])
#
#   Input:  nums = [1, 2, 3]
#   Output: 0  (no subarray sums to 0)
#
# Time Complexity:  O(n)   — Prefix Sum + HashMap
# Space Complexity: O(n)
# ============================================================

#Approach 1: Brute Force
#Check every subarray, track longest one
#Time: O(n^2)
def longest_subarray_0_brute(nums):
    max_length = 0
    for i in range(len(nums)):
        sum = 0
        sum += nums[i]
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == 0:
                length = j - i + 1
                max_length = max(max_length, length)
    return max_length


#Approach 2: Prefix Sum + Hashmap (optimal)
#if prefixSum[i] == prefixSum[j] for i < j, 
#the subarray nums[i+1...j] has sum = 0
#Time: O(n)
def longest_subarray_0_optimal(nums):
    prefix_sum = 0
    max_len = 0
    prefix_map = {0:-1}

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum])
        else:
            prefix_map[prefix_sum] = i
    
    return max_len