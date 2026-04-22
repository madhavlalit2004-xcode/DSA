# ============================================================
# Leetcode 162 - Find Peak Elemnet
# ============================================================
# Given an integer array nums, find a peak element and return
# its index. A peak element is strictly greater than its neighbors.
#
# You may assume nums[-1] = nums[n] = -∞
# If multiple peaks exist, return ANY one of them.
#
# Must run in O(log n) time and O(1) space.
#
# Example:
#   Input:  nums = [1, 2, 3, 1]
#   Output: 2
#
#   Input:  nums = [1, 2, 1, 3, 5, 6, 4]
#   Output: 1 or 5
#
#   Input:  nums = [1]
#   Output: 0
#
# Key Insight:
#   If nums[mid] < nums[mid + 1] → peak lies on right side
#   If nums[mid] > nums[mid + 1] → peak lies on left side (including mid)
#
#   Use slope direction to eliminate half of the array
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Binary Search (optimal)
def peak_element_optimal(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left