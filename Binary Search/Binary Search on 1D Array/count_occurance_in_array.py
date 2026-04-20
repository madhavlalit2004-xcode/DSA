# ============================================================
# Count Occurrences in Sorted Array
# ============================================================
# Given a sorted array nums and a target, return the number
# of times target appears in the array.
#
# Example:
#   Input:  nums = [1, 2, 2, 2, 3, 4], target = 2
#   Output: 3
#
#   Input:  nums = [1, 2, 3, 4, 5], target = 6
#   Output: 0
#
#   Input:  nums = [1, 1, 1, 1, 1], target = 1
#   Output: 5
#
# Note: count = upper_bound(target) - lower_bound(target)
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Linear Search:
#Time: O(n)
def count_occurance_linear(nums, target):
    return nums.count(target)


#Approach 2: Binary Search
#Time: O(n)
def count_occurance_binary(nums, target):
    def find_first(nums, target):
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
    
    def find_last(nums, target):
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <+ right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
    first = find_first(nums, target)
    if first == -1:
        return 0
    last = find_last(nums, target)
    return last - first + 1