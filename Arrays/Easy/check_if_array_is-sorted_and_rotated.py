# ============================================================
# LeetCode 1752 - Check if Array Is Sorted and Rotated
# ============================================================
# Given an array nums, return True if the array was originally
# sorted in non-decreasing order, then rotated some number of
# positions (including zero). Otherwise return False.
#
# Example:
#   Input:  nums = [3, 4, 5, 1, 2]
#   Output: True   (sorted: [1,2,3,4,5] rotated 3 positions)
#
#   Input:  nums = [2, 1, 3, 4]
#   Output: False  (not a rotation of a sorted array)
#
#   Input:  nums = [1, 2, 3]
#   Output: True   (sorted array, rotated 0 positions)
#
#   Input:  nums = [1, 1, 1]
#   Output: True   (duplicates allowed)
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force
#Try all possible rotations and check if any is sorted
#Time: O(n^2)
def check_brute(nums):
    for i in range( len(nums)):
        rotated = nums[i:] + nums[:1]
        for j in range(len(nums) - 1):
            if rotated[j] <= rotated[j+1]:
                return True
    return False


#Approach 2: Count "drop"
#In a sorted + rotated array there is atmost 1 drop 
#a drop is where nums[i] > nums[i+1] % n
#Time: O(n)
def check_optimal(nums):
    n = len(nums)
    drop = 0
    for i in range(n):
        if nums[i] > nums[(i+1) % n]:
            drop += 1
        if drop > 1:
            return False
    return True