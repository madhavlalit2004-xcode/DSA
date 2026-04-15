# ============================================================
# LeetCode 704 - Binary Search
# ============================================================
# Given a sorted array of distinct integers nums and a target,
# return the index of target if found, otherwise return -1.
#
# Example:
#   Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
#   Output: 4
#
#   Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
#   Output: -1
#
#   Input:  nums = [5], target = 5
#   Output: 0
#
# Time Complexity:  O(log n)  — Binary Search
# Space Complexity: O(1)      — Iterative
#                   O(log n)  — Recursive (call stack)
# ============================================================

#Approach 1: Binary Search
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


#Approach 2: Binary Search Recursive
def binary_search_rec(nums, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_rec(nums, target, mid + 1, right)
    else:
        return binary_search_rec(nums, target, left, mid - 1)