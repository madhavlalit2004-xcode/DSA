# ============================================================
# LeetCode 1929 - Concatenation of Array
# ============================================================
# Given an integer array nums of length n, create an array
# ans of length 2n where:
#   ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n
# Return the array ans.
#
# Example:
#   Input:  nums = [1, 2, 1]
#   Output: [1, 2, 1, 1, 2, 1]
#
#   Input:  nums = [1, 3, 2, 1]
#   Output: [1, 3, 2, 1, 1, 3, 2, 1]
#
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================================

#Approacch 1: optimal
def concatenate_array(nums):
    ans = []
    for i in nums:
        ans.append(i)
    for i in nums:
        ans.append(i)
    return ans