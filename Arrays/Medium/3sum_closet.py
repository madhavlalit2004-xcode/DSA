# ============================================================
# LeetCode 16 - 3Sum Closest
# ============================================================
# Given an integer array nums and an integer target,
# find three integers whose sum is closest to target.
# Return the sum of the three integers.
# Exactly one solution is guaranteed.
#
# Example:
#   Input:  nums = [-1, 2, 1, -4], target = 1
#   Output: 2   (sum of [-1, 2, 1] = 2, closest to 1)
#
#   Input:  nums = [0, 0, 0], target = 1
#   Output: 0
#
#   Input:  nums = [1, 1, 1, 1], target = 0
#   Output: 3
#
# Time Complexity:  O(n^2)  — Sort + Two Pointer
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force
def three_sum_closet_brute(nums, target):
    closet = float('inf')
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(closet - target):
                    closet = total
    return closet


#Approach 2: Sort + Two Pointer (optimal)
def three_sum_closet_optimal(nums, target):
    nums.sort()
    closet = float('inf')
    n = len(nums)

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(total - target) < abs(closet - target):
                closet = total
            
            if total == target:
                return target
            elif total < target:
                left += 1
            else:
                right -= 1
    return closet