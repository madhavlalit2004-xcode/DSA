# ============================================================
# LeetCode 34 - Find First and Last Position of Element
# ============================================================
# Given a sorted array nums and a target, return the first and
# last position of target in the array.
# If target is not found, return [-1, -1].
# Must run in O(log n) time.
#
# Example:
#   Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
#   Output: [3, 4]
#
#   Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
#   Output: [-1, -1]
#
#   Input:  nums = [], target = 0
#   Output: [-1, -1]
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Linear Search
def first_and_last_linear(nums, target):
    first = last = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]

#Approach 2: Binary Search
def first_and_second_binary(nums, target):
    def first_find(nums, target):
        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return ans
    
    def last_find(nums, target):
        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid 
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
    if not nums:
        return [-1, -1]
    return [first_find(nums, target), last_find(nums, target)]