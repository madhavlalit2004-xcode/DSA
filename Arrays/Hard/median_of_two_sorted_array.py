# ============================================================
# LeetCode 4 - Median of Two Sorted Arrays
# ============================================================
# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# Example:
#   Input:  nums1 = [1,3], nums2 = [2]
#   Output: 2.0
#
#   Input:  nums1 = [1,2], nums2 = [3,4]
#   Output: 2.5
#
# Approach:
# Use Binary Search on the smaller array to find a correct partition.
# We divide both arrays such that left parts contain smaller elements
# and right parts contain larger elements.
# If partition is valid (left max <= right min), we compute median
# using boundary elements.
#
# Time Complexity:  O(log(min(m, n)))
# Space Complexity: O(1)
# ============================================================

#Approach 1:
def median_optimal(arr1, arr2): 
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2[j]):
        result.append(arr2[j])
        j += 1
    
    left = 0
    right = len(result) - 1

        
    mid = (right + left) // 2
    if len(result) % 2 != 0:
        return result[mid]
    else:
        return (result[mid] + result[mid + 1]) / 2.0