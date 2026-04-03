# ============================================================
# Two Sum
# LeetCode 1 - Two Sum
# ============================================================
# Given an array of integers nums and an integer target,
# return the indices of the two numbers that add up to target.
# You may assume exactly one solution exists.
# You may not use the same element twice.
#
# Example:
#   Input:  nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]  (nums[0] + nums[1] = 2 + 7 = 9)
#
#   Input:  nums = [3, 2, 4], target = 6
#   Output: [1, 2]
#
#   Input:  nums = [3, 3], target = 6
#   Output: [0, 1]
#
# Time Complexity:  O(n)   — HashMap approach
# Space Complexity: O(n)   — HashMap approach
# ============================================================

#Approach 1: Brute Force
#Time: O(n^2)
def two_sum_brute(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


#Approach 2: Hashmaps
#Time: O(n)
def two_sum_optimal(nums, target):
    hash = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in hash:
            return [hash[need], i]
        hash[nums[i]] = i
    return []