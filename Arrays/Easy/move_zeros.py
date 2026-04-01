# ============================================================
# LeetCode 283 - Move Zeroes
# ============================================================
# Given an array nums, move all 0s to the end of it while
# maintaining the relative order of the non-zero elements.
# Must be done in-place without making a copy of the array.
#
# Example:
#   Input:  nums = [0, 1, 0, 3, 12]
#   Output: [1, 3, 12, 0, 0]
#
#   Input:  nums = [0]
#   Output: [0]
#
#   Input:  nums = [1, 0, 0, 2, 3]
#   Output: [1, 2, 3, 0, 0]
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — in-place
# ============================================================

#Approach 1: Brute Force (extra space)
#Time: O(n)
def move_zeroes_brute(nums):
    non_zeros = []
    for num in nums:
        if num != 0:
            non_zeros.append(num)
    for i in range(len(non_zeros)):
        nums[i] = non_zeros[i]
    for i in range(len(non_zeros), len(nums)):
        nums[i] = 0
    return nums

#Approach 2: Two Pointer (optimal)
#Time: Space O(n)
def move_zeros_optimal(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums