# ============================================================
# LeetCode 189 - Rotate Array
# ============================================================
# Given an integer array nums, rotate the array to the right
# by k steps, where k is non-negative.
#
# Example:
#   Input:  nums = [1,2,3,4,5,6,7], k = 3
#   Output: [5,6,7,1,2,3,4]
#
#   Input:  nums = [-1,-100,3,99], k = 2
#   Output: [3,99,-1,-100]
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — optimal (reverse approach)
# ============================================================

#Approach 1: Optimal (Reverse Trick)
#Time: O(n)
def rotate_array_brute(nums, k):
    n = len(nums)
    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    reverse(0, n)
    reverse(0, k - 1)
    reverse(k, n - 1)