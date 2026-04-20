# ============================================================
# LeetCode 81 - Search in Rotated Sorted Array II
# ============================================================
# Same as LeetCode 33 but the array MAY contain duplicates.
# Given a rotated sorted array nums and a target,
# return True if target exists, False otherwise.
#
# Example:
#   Input:  nums = [2, 5, 6, 0, 0, 1, 2], target = 0
#   Output: True
#
#   Input:  nums = [2, 5, 6, 0, 0, 1, 2], target = 3
#   Output: False
#
#   Input:  nums = [1, 0, 1, 1, 1], target = 0
#   Output: True
#
# Key Difference from LC 33:
#   When nums[left] == nums[mid] == nums[right],
#   we CANNOT determine which half is sorted
#   → shrink both pointers by 1 (left++, right--)
#
# Time Complexity:  O(log n) average, O(n) worst case
# Space Complexity: O(1)
# ============================================================

#Aprroach 1:Linear Search:
#Time: O(n)
def search_linear(nums, target):
    if target in nums:
        return True
    else:
        return False


#Approach 2:Binary Search
#Time:O(log n)
def search_optimal(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True
        
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False