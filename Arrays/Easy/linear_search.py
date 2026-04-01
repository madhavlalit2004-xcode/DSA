# ============================================================
# Linear Search
# ============================================================
# Given an array and a target, return the index of the target
# if found, otherwise return -1.
# Search is done sequentially from left to right.
#
# Example:
#   Input:  nums = [3, 1, 7, 2, 9, 4], target = 7
#   Output: 2
#
#   Input:  nums = [3, 1, 7, 2, 9, 4], target = 5
#   Output: -1
#
# Time Complexity:  O(n)  — worst case checks every element
# Space Complexity: O(1)
# ============================================================

#Approach 1: Basic Linear Search
#Scan Left to Right, return index on match
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return 1
    return -1