# ============================================================
# LeetCode 493 - Reverse Pairs
# ============================================================
# Given an integer array nums, return the number of reverse pairs.
# A reverse pair is a pair (i, j) where:
#   0 <= i < j < nums.length AND nums[i] > 2 * nums[j]
#
# Example:
#   Input:  nums = [1, 3, 2, 3, 1]
#   Output: 2   → (3,1) and (3,1)
#
#   Input:  nums = [2, 4, 3, 5, 1]
#   Output: 3   → (2,1), (4,1), (3,1)
#
#   Input:  nums = [5, 4, 3, 2, 1]
#   Output: 4
#
# Time Complexity:  O(n log n)  — Merge Sort approach
# Space Complexity: O(n)
# ============================================================

#Approach 1: Brute Force:
def reverse_pair_brute(nums):
    count = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j] * 2:
                count += 1
    return count


#Approach 2: Merge Sort
def reverse_pairs_optimal(nums):

    def count_and_merge(arr, left, right):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        count = count_and_merge(arr, left, mid) + count_and_merge(arr, mid + 1, right)

        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and arr[i] > 2 * arr[j]:
                j += 1
            count += j - (mid+1)
        
        merged = []
        l, r = left, mid + 1
        while l <= mid and r <= right:
            if arr[l] <= arr[r]:
                merged.append(arr[l])
                l += 1
            else:
                merged.append(arr[r])
                r += 1
        while l <= mid:
            merged.append(arr[l])
            l += 1
        while r <= right:
            merged.append(arr[r])
            r += 1
        
        arr[left:right + 1] = merged 
        return count
    
    nums_copy = nums.copy()
    return count_and_merge(nums_copy, 0, len(nums_copy) - 1)