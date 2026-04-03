# ============================================================
# LeetCode 75 - Sort Colors
# ============================================================
# Given an array nums with n objects colored red, white, or
# blue (represented as 0, 1, 2), sort them in-place so that
# objects of the same color are adjacent in the order 0, 1, 2.
# Must solve without using the built-in sort function.
#
# Also known as the Dutch National Flag Problem.
#
# Example:
#   Input:  nums = [2, 0, 2, 1, 1, 0]
#   Output: [0, 0, 1, 1, 2, 2]
#
#   Input:  nums = [2, 0, 1]
#   Output: [0, 1, 2]
#
#   Input:  nums = [0]
#   Output: [0]
#
# Time Complexity:  O(n)   — single pass (Dutch Flag)
# Space Complexity: O(1)   — in-place
# ============================================================

#Approach 1: Brute Force (sorting)
def sort_colours_brute(nums):
    return nums.sort()


#Approach 2: Dutch National Flag Algo 
def sort_colours_optimal(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1