# ============================================================
# LeetCode 217 - Contains Duplicate
# ============================================================
# Given an integer array nums, return True if any value
# appears at least twice. Return False if all elements
# are distinct.
#
# Example:
#   Input:  nums = [1, 2, 3, 1]
#   Output: True
#
#   Input:  nums = [1, 2, 3, 4]
#   Output: False
#
#   Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
#   Output: True
#
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================================

#Approach 1: Brute Force
def contain_duplicate_brute(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


#Approach 2: HashSet (optimal)
def contain_duplicate_optimal(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False