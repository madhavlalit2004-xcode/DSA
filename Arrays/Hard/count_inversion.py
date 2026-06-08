# ============================================================
# Count Inversions in an Array
# ============================================================
# Given an array nums, count the number of inversions.
# An inversion is a pair (i, j) where i < j but nums[i] > nums[j].
#
# Example:
#   Input:  nums = [2, 4, 1, 3, 5]
#   Output: 3   → (2,1), (4,1), (4,3)
#
#   Input:  nums = [5, 4, 3, 2, 1]
#   Output: 10  → all pairs are inversions
#
#   Input:  nums = [1, 2, 3, 4, 5]
#   Output: 0   → already sorted, no inversions
#
# Time Complexity:  O(n log n)  — Merge Sort
# Space Complexity: O(n)
# ============================================================

#Approach 1: Brute Force
def count_inversion_brute(nums):
    count = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                count += 1
    return count


#Approach 2: Merge Sort
def count_inversion_optimal(nums):

    def merge_count(arr, left, right):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        count = merge_count(arr, left, mid) + merge_count(arr, mid + 1, right)

        merged = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                merged.append(arr[i])
                i += 1
            else:
                count += (mid - i + 1)
                merged.append(arr[j])
                j += 1
            
        while i <= mid:
            merged.append(arr[i])
            i += 1
        while j <= right:
            merged.append(arr[j])
            j += 1
        
        arr[left:right + 1] = merged
        return count
    
    nums_copy = nums.copy()
    return merge_count(nums_copy, 0, len(nums_copy) - 1)