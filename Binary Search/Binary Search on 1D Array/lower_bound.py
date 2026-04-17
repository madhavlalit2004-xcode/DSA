# ============================================================
# Lower Bound
# ============================================================
# Given a sorted array nums and a target, return the index of
# the first element that is >= target (lower bound).
# If no such element exists, return len(nums).
#
# Example:
#   Input:  nums = [1, 2, 4, 4, 5, 6], target = 4
#   Output: 2   (first index where nums[i] >= 4)
#
#   Input:  nums = [1, 2, 4, 4, 5, 6], target = 3
#   Output: 2   (4 is the first element >= 3)
#
#   Input:  nums = [1, 2, 4, 4, 5, 6], target = 7
#   Output: 6   (no element >= 7, return len(nums))
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Linear Search
def lower_bound_linear(nums, target):
    for i in range(0, len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


#Approach 2: Binary Search
#Time: O(log n)
def lower_bound_binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return ans