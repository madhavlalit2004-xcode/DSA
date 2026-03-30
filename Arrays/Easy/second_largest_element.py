# ============================================================
# Second Largest Element in an Array
# ============================================================
# Given an array, find the second largest element in it.
# The second largest must be strictly smaller than the largest.
#
# Example:
#   Input:  [3, 1, 7, 2, 9, 4]
#   Output: 7
#
#   Input:  [10, 20, 5, 100, 50]
#   Output: 50
#
#   Input:  [5, 5, 5]
#   Output: -1  (no second largest exists)
#
# Time Complexity:  O(n)  — single pass (optimal)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force (sorting)
#Time: O(n log n)
def second_largest_brute(nums):
    nums_sorted = sorted(set(nums), reverse=True)
    if len(nums_sorted) < 2:
        return -1
    return nums_sorted[1]


#Approach 2: Two Pass
#Pass 1: Find the largest element
#Pass 2: Find the largest element which is less than largest
#Time: O(n)
def second_largest_2pass(nums):
    largest = max(nums)
    second_lar = float('-inf')
    for num in nums:
        if num != largest and num > second_lar:
            second_lar = num
    return second_lar if second_lar != float('-inf') else -1