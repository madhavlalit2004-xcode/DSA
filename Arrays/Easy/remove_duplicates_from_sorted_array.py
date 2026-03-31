# ============================================================
# LeetCode 26 - Remove Duplicates from Sorted Array
# ============================================================
# Given a sorted array nums, remove duplicates in-place such
# that each unique element appears only once.
# Return the count k of unique elements.
# The first k elements of nums should hold the unique values
# in sorted order.
#
# Example:
#   Input:  nums = [1, 1, 2]
#   Output: 2, nums = [1, 2, _]
#
#   Input:  nums = [0,0,1,1,1,2,2,3,3,4]
#   Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — in-place
# ============================================================

#Approach 1: Brute Force (using extra space)
#Time: O(n)
def remove_duplicates_brute(nums):
    arr = []
    for i in nums:
        if nums[i] not in arr:
            arr.append(i)
    return arr


#Approach 2: Two Pointers
#Time O(n)
#Space O(1)
def remove_duplicate_optimal(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1