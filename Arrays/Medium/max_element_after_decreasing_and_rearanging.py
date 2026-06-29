# ============================================================
# LeetCode 1846 - Maximum Element After Decreasing and Rearranging
# ============================================================
# Given an array arr, perform these operations any number of times:
#   - Rearrange elements in any order
#   - Decrease any element to any positive integer
# Goal: make the array satisfy:
#   - arr[0] == 1
#   - |arr[i] - arr[i-1]| <= 1 for all i
# Return the maximum possible value of any element.
#
# Example:
#   Input:  arr = [2, 2, 1, 2, 1]
#   Output: 2
#
#   Input:  arr = [100, 1, 1000]
#   Output: 3
#
#   Input:  arr = [1, 2, 3, 4, 5]
#   Output: 5
#
# Key Insight:
#   Sort the array. The maximum value at index i is at most i+1.
#   So greedily assign each position the minimum of arr[i] and prev+1.
#
# Time Complexity:  O(n log n)  — sorting dominates
# Space Complexity: O(1)
# ============================================================


#Approach 1: sort + track max
def max_element_optimal(nums):
    nums.sort()
    nums[0] = 1

    for i in range(1, len(nums)):
        nums[i] = min(nums[i], nums[i-1] + 1)

    return nums[-1]