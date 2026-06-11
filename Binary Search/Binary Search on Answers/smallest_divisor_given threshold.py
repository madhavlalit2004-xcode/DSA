# ============================================================
# LeetCode 1283 - Find the Smallest Divisor Given a Threshold
# ============================================================
# You are given an array of integers nums and an integer threshold.
#
# You need to choose a positive integer divisor such that:
# sum of (ceil(nums[i] / divisor)) for all i <= threshold
#
# Return the smallest divisor that satisfies this condition.
#
# Example:
#   Input:  nums = [1,2,5,9], threshold = 6
#   Output: 5
#
#   Input:  nums = [44,22,33,11,1], threshold = 5
#   Output: 44
#
# Approach (Brute Force):
# - Try divisor from 1 to max(nums)
# - For each divisor, compute sum:
#       sum += ceil(num / divisor)
# - Return smallest divisor where sum <= threshold
#
# Time Complexity:  O(n * max(nums))
# Space Complexity: O(1)
#
# Approach (Optimal - Binary Search):
# - Search divisor in range [1, max(nums)]
# - For each mid:
#       compute sum = ceil(nums[i] / mid)
# - If sum <= threshold → try smaller divisor
# - Else → increase divisor
#
# Time Complexity:  O(n * log(max(nums)))
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force
def smallest_div_brute(nums, threshold):
    for d in range(1, max(nums) + 1):
        total = 0
        for num in nums:
            total += (num + d - 1) // d
        
        if total <= threshold:
            return d


#Approach 2: Optimal
def smallest_div_optimal(nums, threshold):
    def compute_sum(divisor):
        for num in nums:
            total += (num + divisor - 1) // divisor
        return total 
    
    low = 1
    high = max(nums)

    while low <= high:
        mid = (low + high) // 2
        if compute_sum(mid) <= threshold:
            high = mid - 1
        else:
            low = mid + 1
    return low