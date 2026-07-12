# ============================================================
# LeetCode 347 - Top K Frequent Elements
# ============================================================
# Given an integer array nums and an integer k, return the k
# most frequent elements. You may return the answer in any order.
#
# Example:
#   Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
#   Output: [1, 2]
#
#   Input:  nums = [1], k = 1
#   Output: [1]
#
# Time Complexity:  O(n log k)  — Heap approach
# Space Complexity: O(n)
# ============================================================

#Approach 1: Optimal
def top_k_frequent_optimal(nums, k):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    sorted_list = sorted(freq.items(), key = lambda x: x[1], reverse=True)

    result = []

    for i in range(k):
        result.append(sorted_list[i][0])
    
    return result