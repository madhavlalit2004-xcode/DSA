# ============================================================
# LeetCode 27 - Remove Element
# ============================================================
# Given an array nums and a value val, remove all occurrences
# of val in-place. Return the count k of elements not equal
# to val. The first k elements of nums should hold the result.
#
# Example:
#   Input:  nums = [3, 2, 2, 3], val = 3
#   Output: 2, nums = [2, 2, _, _]
#
#   Input:  nums = [0,1,2,2,3,0,4,2], val = 2
#   Output: 5, nums = [0,1,3,0,4,_,_,_]
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — in-place
# ============================================================

#Approach 1: Brute Force (extra space)
#Time: O(n)
def remove_element_brute(nums, val):
    result = [x for x in nums if x != val]
    for i in range(len(result)):
        nums[i] = result[i]
    return len(result)


#Approach 2: Two Pointer
#time: O(n)
def remove_element_optimal(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k