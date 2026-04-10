# ============================================================
# LeetCode 18 - 4Sum
# ============================================================
# Given an array nums and an integer target, return all unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that
# a, b, c, d are distinct indices and their sum equals target.
#
# Example:
#   Input:  nums = [1, 0, -1, 0, -2, 2], target = 0
#   Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#   Input:  nums = [2, 2, 2, 2, 2], target = 8
#   Output: [[2,2,2,2]]
#
#   Input:  nums = [1, -2, -5, -4, -3, 3, 3, 5], target = -11
#   Output: [[-5,-4,-3,1]]
#
# Time Complexity:  O(n^3)  — Sort + Two Pointer
# Space Complexity: O(1)    — ignoring output array
# ============================================================

#Approach 1: BruteForce
#Check every quadriplet avoid duplicate using a set
#Time: O(n^4)
def four_sum_brute(nums, target):
    result = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        quad = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                        result.add(quad)
    return [list(q) for q in result]


#Approach 2: Sort + twoPointer
#Time: O(n^3)
def four_pointer_optimal(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                    
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result 

print(four_pointer_optimal([1, 0, -1, 0, -2, 2], 0))