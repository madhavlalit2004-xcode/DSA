# ============================================================
# Split Array Largest Sum
# ============================================================
# Given an integer array nums and an integer k,
# split nums into k non-empty continuous subarrays such that
# the largest sum among these subarrays is MINIMIZED.
#
# Return the minimized largest subarray sum.
#
# Example:
#   Input:  nums = [7, 2, 5, 10, 8], k = 2
#   Output: 18
#   Explanation:
#     Split as [7, 2, 5] and [10, 8]
#     Subarray sums are 14 and 18
#     Largest sum = 18, which is minimized
#
#   Input:  nums = [1, 2, 3, 4, 5], k = 2
#   Output: 9
#   Explanation:
#     Split as [1, 2, 3] and [4, 5]
#     Subarray sums are 6 and 9
#     Largest sum = 9
#
# Key Insight:
#   Binary search on the ANSWER.
#
#   The answer is the maximum allowed subarray sum.
#
#   Minimum possible answer = max(nums)
#     Because every element must belong to some subarray.
#
#   Maximum possible answer = sum(nums)
#     Because we can take the whole array as one subarray.
#
#   For a given max_sum, greedily check how many subarrays
#   are needed if no subarray sum is allowed to exceed max_sum.
#
#   If required subarrays <= k:
#     max_sum is possible, try smaller answer.
#
#   If required subarrays > k:
#     max_sum is too small, increase it.
#
# Time Complexity:  O(n * log(sum(nums) - max(nums)))
# Space Complexity: O(1)
# ============================================================

#Approach 1: Binary Search (optimal)
def split_array(nums, k):
    def can_split(max_sum):
        subarray = 1
        current_sum = 0

        for num in nums:
            if current_sum + num <= max_sum:
                current_sum += num
            else:
                subarray += 1
                current_sum = num

                if subarray > k:
                    return False
        return True
    

    left =  max(nums)
    right = sum(nums)
    answer = right

    while left <= right:
        mid = left + (right - left) // 2

        if can_split(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer