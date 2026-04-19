# ============================================================
# Floor and Ceil in Sorted Array
# ============================================================
# Given a sorted array nums and a target:
#   Floor → largest element in nums <= target  (-1 if none)
#   Ceil  → smallest element in nums >= target (-1 if none)
#
# Example:
#   Input:  nums = [1, 2, 4, 6, 10, 12], target = 5
#   Output: Floor = 4, Ceil = 6
#
#   Input:  nums = [1, 2, 4, 6, 10, 12], target = 4
#   Output: Floor = 4, Ceil = 4  (exact match)
#
#   Input:  nums = [1, 2, 4, 6, 10, 12], target = 0
#   Output: Floor = -1, Ceil = 1
#
#   Input:  nums = [1, 2, 4, 6, 10, 12], target = 15
#   Output: Floor = 12, Ceil = -1
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Linear Search
def floor_ceil_linear(nums, target):
    floor = -1
    ceil = -1

    for i in nums:
        if i <= target:
            floor = i
    
        if ceil == -1 and i >= target:
            ceil = i
    return floor, ceil


#Approach 2: Binary Search
def find_floor(nums, target):
    left = 0
    right = len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left +right) // 2
        if nums[mid] <= target:
            ans = nums[mid]
            left = mid + 1
        else:
            right = mid - 1
    return ans

def find_ceil(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] >= target:
            ans = nums[mid]
            right = mid - 1
        else:
            left = mid + 1
    return ans

def floor_ceil_binary(nums, target):
    return find_floor(nums, target), find_ceil(nums, target)