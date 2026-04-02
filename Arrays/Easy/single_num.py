# ============================================================
# Single Number
# LeetCode 136 - Single Number
# ============================================================
# Given a non-empty array of integers nums, every element
# appears twice except for one. Find that single one.
# Must be solved with O(n) time and O(1) extra space.
#
# Example:
#   Input:  nums = [2, 2, 1]
#   Output: 1
#
#   Input:  nums = [4, 1, 2, 1, 2]
#   Output: 4
#
#   Input:  nums = [1]
#   Output: 1
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — XOR approach
# ============================================================

#Approach 1: Brute Force (using hashmaps)
#Time : O(n)
def single_num_hashmap(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for num, count in freq.items():
        if count == 1:
            return num
        

#Approach 2: Using XOR
#Time: O(n)
def single_num_xor(nums):
    result = 0
    for i in nums:
        result ^= i
    return result