# ============================================================
# LeetCode 912 - Sort an Array
# ============================================================
# Given an array of integers nums, sort the array in ascending
# order and return it. Must not use built-in sort functions.
# Must run in O(n log n) time and O(1) extra space.
#
# Example:
#   Input:  nums = [5, 2, 3, 1]
#   Output: [1, 2, 3, 5]
#
#   Input:  nums = [5, 1, 1, 2, 0, 0]
#   Output: [0, 0, 1, 1, 2, 5]
#
# ============================================================

#Approach 1: Merge Sort (optimal)
def sort_merge(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = sort_merge(nums[:mid])
    right = sort_merge(nums[mid:])

    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged