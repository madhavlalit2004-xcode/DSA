# ============================================================
# Longest Consecutive Sequence
# LeetCode 128 - Longest Consecutive Sequence
# ============================================================
# Given an unsorted array of integers nums, return the length
# of the longest consecutive elements sequence.
# Must run in O(n) time.
#
# Example:
#   Input:  nums = [100, 4, 200, 1, 3, 2]
#   Output: 4  (sequence: [1, 2, 3, 4])
#
#   Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
#   Output: 9  (sequence: [0, 1, 2, 3, 4, 5, 6, 7, 8])
#
#   Input:  nums = [1]
#   Output: 1
#
# Time Complexity:  O(n)   — HashSet approach
# Space Complexity: O(n)
# ============================================================

#Approach 1: Brute Force
#Sort the array, count the consecutive streak
def longest_consecutive_brute(nums):
    if not nums:
        return 0
    num_sorted = sorted(set(nums))
    max_len = 1
    count = 1
    for i in range(1, num_sorted):
        if num_sorted[i] == num_sorted[i-1] + 1:
            count += 1
            max_len(max_len, count)
        else:
            count = 1
    return max_len


#Approach 2: hashset
#Add all elements to a set for O(1) lookup
def longest_consecutive_optimal(nums):
    if not nums:
        return 0
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            max_len = max(max_len, streak)
    return max_len