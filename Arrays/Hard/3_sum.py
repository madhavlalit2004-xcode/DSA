# ============================================================
# LeetCode 15 - 3Sum
# ============================================================
# Given an integer array nums, return all triplets
# [nums[i], nums[j], nums[k]] such that i != j != k
# and nums[i] + nums[j] + nums[k] == 0.
# The solution set must not contain duplicate triplets.
#
# Example:
#   Input:  nums = [-1, 0, 1, 2, -1, -4]
#   Output: [[-1, -1, 2], [-1, 0, 1]]
#
#   Input:  nums = [0, 1, 1]
#   Output: []
#
#   Input:  nums = [0, 0, 0]
#   Output: [[0, 0, 0]]
#
# Time Complexity:  O(n^2)  — Two Pointer approach
# Space Complexity: O(1)    — ignoring output array
# ============================================================

#Approach 1: Brute Force
#Check every triplet and avoid duplicate using a set
#Time: O(n^3)
def three_sum_brute(nums):
    result = set()
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)
    return [list(t) for t in result]


#Approach 2: Sort + Two Pointer
#Sort the array, fix one elemnt, use two pointer for the rest
#Skip duplicates at every level to avoid duplicate triplet
#Time o(n^2)
def three_sum_optimal(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right -1]:
                    right -= 1
                
                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1
    return result