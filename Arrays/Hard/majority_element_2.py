# ============================================================
# LeetCode 229 - Majority Element II
# ============================================================
# Given an integer array nums, return all elements that appear
# more than n/3 times. There can be at most 2 such elements.
#
# Example:
#   Input:  nums = [3, 2, 3]
#   Output: [3]
#
#   Input:  nums = [1, 2]
#   Output: [1, 2]
#
#   Input:  nums = [1, 1, 1, 3, 3, 2, 2, 2]
#   Output: [1, 2]
#
# Time Complexity:  O(n)   — Extended Boyer-Moore
# Space Complexity: O(1)
# ============================================================

#Approach 1: HashMap
def majority_element_2(nums):
    freq = {}
    result = []
    for i in nums:
        freq[i] = freq.get(i+0) + 1
    
    for num, count in freq.items():
        if count > len(nums) // 3:
            result.append(num)
    return result