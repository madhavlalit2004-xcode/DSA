# ============================================================
# LeetCode 1299 - Replace Elements with Greatest Element on Right Side
# ============================================================
# Given an array arr, replace every element in that array with
# the greatest element among the elements to its right.
# Replace the last element with -1.
# Return the modified array.
#
# Example:
#   Input:  arr = [17, 18, 5, 4, 6, 1]
#   Output: [18, 6, 6, 6, 1, -1]
#
#   Input:  arr = [400]
#   Output: [-1]
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — in-place
# ============================================================

#Approach 1: BruteForce 
def replace_elements_brute(arr):
    n = len(arr)
    for i in range(n -1):
        arr[i] = max(arr[i+1:])
    arr[-1] = -1
    return arr


#Approach 2: Scan From Right (optimal):
def replace_elements_optimal(arr):
    max_right = -1
    for i in range(len(arr) - 1, -1, -1):
        new_max = max(max_right, arr[i])
        arr[i] = max_right
        max_right = new_max

    return arr