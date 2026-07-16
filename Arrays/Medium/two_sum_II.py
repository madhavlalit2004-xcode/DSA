# ============================================================
# LeetCode 167 - Two Sum II - Input Array Is Sorted
# ============================================================
# Given a 1-indexed sorted array numbers and a target,
# return indices [i, j] (1-indexed) of the two numbers
# that add up to target. Exactly one solution guaranteed.
# Must use only O(1) extra space.
#
# Example:
#   Input:  numbers = [2, 7, 11, 15], target = 9
#   Output: [1, 2]   (numbers[0] + numbers[1] = 2 + 7 = 9)
#
#   Input:  numbers = [2, 3, 4], target = 6
#   Output: [1, 3]   (numbers[0] + numbers[2] = 2 + 4 = 6)
#
#   Input:  numbers = [-1, 0], target = -1
#   Output: [1, 2]
#
# Time Complexity:  O(n)   — Two Pointer
# Space Complexity: O(1)

#Approach 1: Brute Force
def two_sum_ii_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i+1, j+1]
    return []

#Approach 2: Two Pointer (optimal)
def two_sum_ii(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1