# ============================================================
# LeetCode 153 - Find Minimum in Rotated Sorted Array
# ============================================================
# Given a sorted rotated array nums of unique elements,
# return the minimum element.
#
# Example:
#   Input:  nums = [3, 4, 5, 1, 2]
#   Output: 1
#
#   Input:  nums = [4, 5, 6, 7, 0, 1, 2]
#   Output: 0
#
#   Input:  nums = [11, 13, 15, 17]
#   Output: 11  (not rotated — min is at index 0)
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Linear Search
def find_min_linear(nums):
    return min(nums)


#Approach 2:Binary Search
def find_min_optimal(nums):
    left = 0
    right = len(nums) - 1
    ans = float('inf')

    while left <= right:
        if nums[left] <= nums[right]:
            ans = min(ans, nums[left])
            break

        mid = (left + right) // 2
        ans = min(ans, nums[mid])

        if nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return ans