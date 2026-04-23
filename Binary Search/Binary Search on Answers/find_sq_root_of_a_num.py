# ============================================================
# LeetCode 69 - Sqrt(x)
# ============================================================
# Given a non-negative integer x, return the square root of x
# rounded down to the nearest integer (floor sqrt).
# Do not use built-in exponent functions or operators.
#
# Example:
#   Input:  x = 4
#   Output: 2
#
#   Input:  x = 8
#   Output: 2  (sqrt(8) = 2.82... → floor = 2)
#
#   Input:  x = 0
#   Output: 0
#
# Time Complexity:  O(log n)  — Binary Search
# Space Complexity: O(1)
# ============================================================


#Approach 1:Binary Search(optimal)
def sq_root_optimal(x):
    if x == 0:
        return 0
    left = 1
    right = x
    ans = 1

    while left <= right:
        mid = (left + right) // 2
        if mid*mid <= x:
            ans = mid
            left = mid - 1
        else:
            right = mid + 1
    return ans