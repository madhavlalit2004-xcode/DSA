# ============================================================
# LeetCode 88 - Merge Sorted Array
# ============================================================
# You are given two sorted integer arrays nums1 and nums2.
# nums1 has a length of m + n where first m elements are valid
# and last n elements are 0 (placeholders).
# Merge nums2 into nums1 in-place in sorted order.
#
# Example:
#   Input:  nums1 = [1,2,3,0,0,0], m = 3
#           nums2 = [2,5,6],        n = 3
#   Output: [1,2,2,3,5,6]
#
#   Input:  nums1 = [1], m = 1, nums2 = [], n = 0
#   Output: [1]
#
#   Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
#   Output: [1]
#
# Time Complexity:  O(m + n)  — Three Pointer approach
# Space Complexity: O(1)      — in-place
# ============================================================

#Approach 1: Brute Force
#Time: O((m+n) + log(m+n))
def merge_brute(nums1, m, nums2, n):
    for i in range(n):
        nums1[m+i] = nums2[i]
    nums1.sort() 


#Approach 2: Three pointer from end (optimal)
#Time: O(m+n)
def merge_optimal(nums1, m, nums2, n):
    i = m-1
    j = n-1
    k = m+n-1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1