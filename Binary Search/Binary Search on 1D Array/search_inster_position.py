# ============================================================
# LeetCode 35 - Search Insert Position
# ============================================================
# Given a sorted array of distinct integers nums and a target,
# return the index if target is found. If not, return the index
# where it would be inserted to keep the array sorted.
#
# Example:
#   Input:  nums = [1, 3, 5, 6], target = 5
#   Output: 2
#
#   Input:  nums = [1, 3, 5, 6], target = 2
#   Output: 1
#
#   Input:  nums = [1, 3, 5, 6], target = 7
#   Output: 4
#
#   Input:  nums = [1, 3, 5, 6], target = 0
#   Output: 0
#
# Note: This is exactly the Lower Bound problem!
#       Answer = first index where nums[i] >= target
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Linear Search
def search_inster_linear(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


#Approach 2: Binary Search
def search_insert_binary(nums, target):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
    
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return ans