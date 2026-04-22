# ============================================================
# LeetCode 540 - Single Element in a Sorted Array
# ============================================================
# Given a sorted array where every element appears exactly
# twice except for one element which appears once.
# Return the single element.
# Must run in O(log n) time and O(1) space.
#
# Example:
#   Input:  nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
#   Output: 2
#
#   Input:  nums = [3, 3, 7, 7, 10, 11, 11]
#   Output: 10
#
#   Input:  nums = [1]
#   Output: 1
#
# Key Insight:
#   Before the single element → pairs start at even indices
#   After  the single element → pairs start at odd  indices
#   Use this to decide which half to search
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Binary Search
def single_element_optimal(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 1:
            mid -= 1
        
        if nums[mid] == nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return nums[left]