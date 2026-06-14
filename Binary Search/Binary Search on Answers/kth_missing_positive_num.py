# ============================================================
# LeetCode 1539 - Kth Missing Positive Number
# ============================================================
# Given a strictly increasing array arr of positive integers
# and an integer k, return the kth missing positive number.
#
# Example:
#   Input:  arr = [2, 3, 4, 7, 11], k = 5
#   Output: 9
#   Missing: [1, 5, 6, 8, 9, 10, ...] → 5th missing = 9
#
#   Input:  arr = [1, 2, 3, 4], k = 2
#   Output: 6
#   Missing: [5, 6, 7, ...] → 2nd missing = 6
#
# Key Insight:
#   At index i, arr[i] should ideally be i+1 (1-indexed)
#   Missing count before arr[i] = arr[i] - (i + 1)
#   Binary search for the first index where missing count >= k
#
# Time Complexity:  O(log n)  — Binary Search
# Space Complexity: O(1)
# ============================================================

#Approach 1: Binary Search (optimal)
def kth_missing_num_optimal(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1
    
    return left + k