# ============================================================
# LeetCode 152 - Maximum Product Subarray
# ============================================================
# Given an integer array nums, find a subarray that has the
# largest product and return the product.
#
# Example:
#   Input:  nums = [2, 3, -2, 4]
#   Output: 6  (subarray [2, 3])
#
#   Input:  nums = [-2, 0, -1]
#   Output: 0
#
#   Input:  nums = [-2, 3, -4]
#   Output: 24  (subarray [-2, 3, -4])
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force
#Time: O(n^2)
def max_product(nums):
    max_prod = float('-inf')
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            max_prod = max(max_prod, product)
    return max_prod


#Approach 2: Track min and max (optimal)
#Time: O(n)
def max_product_optimal(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for num in nums[1:]:
        candidate = (num, max_prod*num, min_prod*num)
        max_prod = max(candidate)
        min_prod = min(candidate)
        result = max(max_prod, result)
    return result
