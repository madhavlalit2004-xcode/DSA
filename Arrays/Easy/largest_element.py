# ============================================================
# Largest Element in an Array
# ============================================================
# Given an array, find and return the largest element in it.
#
# Example:
#   Input:  [3, 1, 7, 2, 9, 4]
#   Output: 9
#
#   Input:  [10, 20, 5, 100, 50]
#   Output: 100
#
#   Input:  [-3, -1, -7]
#   Output: -1
#
# Time Complexity:  O(n)  — single pass through array
# Space Complexity: O(1)  — no extra space used
# ============================================================

#Approach 1: Linear Search
def largest_element_linear(nums):
    largest = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    return largest


#Approach 2: Using built in max()
def largest_builtin(nums):
    return max(nums)