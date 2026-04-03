# ============================================================
# LeetCode 169 - Majority Element
# ============================================================
# Given an array nums of size n, return the majority element.
# The majority element appears more than n/2 times.
# You may assume the majority element always exists.
#
# Example:
#   Input:  nums = [3, 2, 3]
#   Output: 3
#
#   Input:  nums = [2, 2, 1, 1, 1, 2, 2]
#   Output: 2
#
#   Input:  nums = [1]
#   Output: 1
#
# Time Complexity:  O(n)   — Boyer-Moore Voting Algorithm
# Space Complexity: O(1)   — Boyer-Moore Voting Algorithm
# ============================================================

#Approach 1: Brute Force
#Time = O(n^2)
def majority_element_brute(nums):
    n = len(nums)
    for num in nums:
        count = nums.count(num)
        if count > n // 2:
            return num
    return -1


#Approach 2: Hashmaps
#Time: O(n)
def majority_element_optimal(nums):
    freq = {}
    n = len(nums)
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num
    return -1