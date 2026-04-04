# ============================================================
# Union of Two Sorted Arrays
# ============================================================
# Given two sorted arrays, return their union — a sorted array
# of all distinct elements present in either array.
#
# Example:
#   Input:  a = [1, 2, 3, 4, 5], b = [1, 2, 7]
#   Output: [1, 2, 3, 4, 5, 7]
#
#   Input:  a = [1, 1, 2, 3], b = [2, 3, 4, 5]
#   Output: [1, 2, 3, 4, 5]
#
#   Input:  a = [1, 2, 3], b = [4, 5, 6]
#   Output: [1, 2, 3, 4, 5, 6]
#
# Time Complexity:  O(m + n)  — two pointer approach
# Space Complexity: O(m + n)  — result array
# ============================================================

#Approach 1: Brute Force (using stes)
#Time: O((m+n) log(m+n))
def union_brute(a, b):
    return sorted(set(a) | set(b))


#Approach 2: Two Pointer (optimal)
def union_two_pointer(a, b):
    i, j = 0, 0
    result = []
 
    while i < len(a) and j < len(b):
        if i > 0 and a[i] == a[i - 1]:
            i += 1
            continue

        if j > 0 and b[j] == b[j - 1]:
            j += 1
            continue
 
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:                          
            result.append(a[i])
            i += 1
            j += 1
 
    while i < len(a):
        if not result or a[i] != result[-1]:
            result.append(a[i])
        i += 1

    while j < len(b):
        if not result or b[j] != result[-1]:
            result.append(b[j])
        j += 1
 
    return result

print(union_two_pointer([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))