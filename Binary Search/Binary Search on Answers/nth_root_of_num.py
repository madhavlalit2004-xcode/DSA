# ============================================================
# Nth Root of a Number using Binary Search
# ============================================================
# Given two integers n and m, find the nth root of m.
# That is, find x such that:
#        x^n = m
#
# If the exact root does not exist, return -1 (for integer case)
# OR return approximate value (for decimal case).
#
# Example:
#   Input:  n = 3, m = 27
#   Output: 3
#
#   Input:  n = 2, m = 10
#   Output: -1  (no exact integer root)
#
# Approach (Brute Force):
# - Try all numbers from 1 to m
# - Check if i^n == m
#
# Time Complexity:  O(m * log n)
# Space Complexity: O(1)
#
# Approach (Optimal - Binary Search):
# - Search in range [1, m]
# - For mid, compute mid^n
# - If mid^n == m → return mid
# - If mid^n < m → move right
# - Else → move left
#
# Time Complexity:  O(log m * log n)
# Space Complexity: O(1)
# ============================================================

#Aapproach 1: Brute Force
def nth_root_brute(n, m):
    for i in range(1, m + 1):
        if i ** n == m:
            return i
    return -1


#Approach 2: Binary Search
def nth_root_optimal(n, m):
    low, high = 1, m
    while low <= high:
        mid = (low + high) // 2
        ans = 1
        for _ in range(n):
            ans *= mid
            if ans > m:
                break
        
        if ans == mid:
            return mid
        
        if ans < mid:
            low = mid + 1
        
        else:
            high = mid + 1
        
    return -1
