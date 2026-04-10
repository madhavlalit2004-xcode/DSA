# ============================================================
# LeetCode 118 - Pascal's Triangle
# ============================================================
# Given an integer numRows, return the first numRows of
# Pascal's triangle. Each number is the sum of the two
# numbers directly above it.
#
# Example:
#   Input:  numRows = 5
#   Output: [[1],
#             [1,1],
#             [1,2,1],
#             [1,3,3,1],
#             [1,4,6,4,1]]
#
#   Input:  numRows = 1
#   Output: [[1]]
#
# Time Complexity:  O(n^2)
# Space Complexity: O(n^2)
# ============================================================

#Approach 1: Build each row from prev row
#Time: O(n^2)
def pascal_triangle_optimal(numRows):
    result = []

    for i in range(numRows):
        row = [1] * (i+1)

        for j in range(1, i):
            row[j] = result[i-1][j-1] + result[i-1][j]

        result.append(row)
    return result