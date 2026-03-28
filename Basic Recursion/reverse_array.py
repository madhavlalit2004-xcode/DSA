# ============================================================
# Reverse an Array Using Recursion
# ============================================================
# Given an array, reverse it in-place using recursion
# without any loops.
#
# Example:
#   Input:  [1, 2, 3, 4, 5]
#   Output: [5, 4, 3, 2, 1]
#
#   Input:  [1, 2, 3, 4]
#   Output: [4, 3, 2, 1]
#
#   Input:  [1]
#   Output: [1]
#
# Time Complexity:  O(n)  — n/2 recursive calls
# Space Complexity: O(n)  — n frames on the call stack
# ============================================================

#Approach 1: Two Pointers
def reverse_array(arr, left, right):
    left = 0
    right = len(arr) - 1
    if left >= right:
        return 
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array(arr, left + 1, right - 1)