# ============================================================
# Find Highest and Lowest Frequency Element in Array
# ============================================================
# Given an array, find the element that appears the most
# and the element that appears the least using hashing.
#
# Example:
#   Input:  [1, 2, 1, 3, 2, 1, 4]
#   Output: Highest Freq → 1 (appears 3 times)
#           Lowest Freq  → 3 (appears 1 time)
#
#   Input:  [10, 10, 10, 5, 5, 3]
#   Output: Highest Freq → 10 (appears 3 times)
#           Lowest Freq  → 3  (appears 1 time)
#
# Time Complexity:  O(n)  — single pass to build freq map
# Space Complexity: O(n)  — hash map storage
# ============================================================

#Approach 1: Manual Hashing + Linear Search for min/max
def high_low_freq(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    max_freq = max(freq.values())
    min_freq = min(freq.values())

    highest = [k for k, v in freq.items() if v == max_freq]
    lowest = [k for k, v in freq.items() if v == min_freq]

    return highest, max_freq, lowest, min_freq