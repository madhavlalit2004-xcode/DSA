# ============================================================
# Finding the Missing Number
# LeetCode 268 - Missing Number
# ============================================================
# Given an array nums containing n distinct numbers in the
# range [0, n], return the only number in the range missing.
#
# Example:
#   Input:  nums = [3, 0, 1]
#   Output: 2
#
#   Input:  nums = [0, 1]
#   Output: 2
#
#   Input:  nums = [9,6,4,2,3,5,7,0,1]
#   Output: 8
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — optimal approach
# ============================================================

#Approach 1: Sorting
#Time = O(n log n)
def missing_nums_brute(nums):
    nums_sorted = sorted(nums)
    for i in range(len(nums_sorted)):
        if nums_sorted[i] != i:
            return i
    return len(nums)


#Approach 2: Sum Formula
#Expected sum of [0....n] = n*(n+1)/2
#Missing num = expected sum - actual sum
def missing_num_sum(nums):
    n = len(nums)
    expected = n*(n-1) // 2
    return expected - sum(nums)


#Approach 3: XOR
def missing_num_xor(nums):
    xor = 0
    for i in range(len(nums) + 1):
        xor ^= i
    for num in nums:
        xor ^= num
    return xor