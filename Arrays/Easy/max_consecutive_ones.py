# ============================================================
# Max Consecutive Ones
# LeetCode 485 - Max Consecutive Ones
# ============================================================
# Given a binary array nums, return the maximum number of
# consecutive 1s in the array.
#
# Example:
#   Input:  nums = [1, 1, 0, 1, 1, 1]
#   Output: 3
#
#   Input:  nums = [1, 0, 1, 1, 0, 1]
#   Output: 2
#
#   Input:  nums = [1, 1, 1, 1]
#   Output: 4
#
# Time Complexity:  O(n)  — single pass
# Space Complexity: O(1)
# ============================================================

#Approach 1: Single pass
def max_consecutive(nums):
    count = 0
    max_count = 0
    for i in nums:
        if i == 1:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0
    return max_count