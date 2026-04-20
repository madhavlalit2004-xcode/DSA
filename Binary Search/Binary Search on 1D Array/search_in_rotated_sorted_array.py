# ============================================================
# LeetCode 33 - Search in Rotated Sorted Array
# ============================================================
# Given a rotated sorted array nums (with distinct values)
# and a target, return the index of target if found,
# otherwise return -1.
#
# Example:
#   Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
#   Output: 4
#
#   Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
#   Output: -1
#
#   Input:  nums = [1], target = 0
#   Output: -1
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Linear Search
#Time: O(n)
def search_linear(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


#Approach 2: Binary Search:
#Time: O(log n)
def search_optimal(nums, target):
    left = 0
    right = len(nums) - 1
    ans = -1

    while left <= right :
        mid = (left + right) - 1
        if nums[mid] == target:
            ans = mid
    if nums[mid] <= nums[left]:
        if nums[left] <= target < nums[mid]:
            right = mid + 1
        else:
            left = mid - 1
    
    else:
        if nums[mid] < target <= nums[right]:
            left = mid - 1
        else:
            right = mid + 1
    
    return ans