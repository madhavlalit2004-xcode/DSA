# ============================================================
# Count Frequency of Each Element in Array Using Hashing
# ============================================================
# Given an array, count how many times each element appears
# using hashing techniques.
#
# Example:
#   Input:  [1, 2, 1, 3, 2, 1, 4]
#   Output: {1: 3, 2: 2, 3: 1, 4: 1}
#
#   Input:  [10, 10, 10, 5, 5]
#   Output: {10: 3, 5: 2}
#
# Time Complexity:  O(n)  — single pass through array
# Space Complexity: O(n)  — hash map storage
# ============================================================

#Approach 1: Hashing using dict
def count_freq_of_num(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


#Approach 2: Hashing using dict.get()
def count_freq_of_n(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    return freq