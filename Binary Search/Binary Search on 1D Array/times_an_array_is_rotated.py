# ============================================================
# Find How Many Times a Sorted Array is Rotated
# ============================================================
# A sorted array is rotated k times. Find k.
# The number of rotations = index of the minimum element.
#
# Example:
#   Input:  nums = [4, 5, 6, 7, 0, 1, 2]
#   Output: 4   (rotated 4 times → min at index 4)
#
#   Input:  nums = [3, 4, 5, 1, 2]
#   Output: 3   (rotated 3 times → min at index 3)
#
#   Input:  nums = [1, 2, 3, 4, 5]
#   Output: 0   (not rotated → min at index 0)
#
#   Input:  nums = [2, 1]
#   Output: 1
#
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# ============================================================

#Approach 1:Linear Search
def time_rot_linear(nums):
    min_val = min(nums)
    return nums.index(min_val)


#Approach 2: Binary Search(optimal)
#Num of rotations = index of min element
def time_rot_optimal(nums):
    left = 0
    right = len(nums) - 1
    
    if nums[left] <= nums[right]:
        return 0
    
    while left <+ right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left