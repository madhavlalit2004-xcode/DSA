# ============================================================
# Leaders in an Array
# ============================================================
# An element is a leader if it is greater than all elements
# to its right. The rightmost element is always a leader.
#
# Example:
#   Input:  nums = [16, 17, 4, 3, 5, 2]
#   Output: [17, 5, 2]
#
#   Input:  nums = [1, 2, 3, 4, 5]
#   Output: [5]   (only the last element)
#
#   Input:  nums = [5, 4, 3, 2, 1]
#   Output: [5, 4, 3, 2, 1]   (all are leaders)
#
# Time Complexity:  O(n)   — right to left pass
# Space Complexity: O(n)   — result list
# ============================================================

#Approach 1: Brute Force
#Time: O(n^2)
def leader_brute(nums):
    leader1 = nums[len(nums)-1]
    result = []
    for i in range(0, len(nums)):
        is_leader = True
        for j in range(i+1, len(nums)):
            if nums[j] >= nums[i]:
                is_leader = False
                break
        if is_leader:
            result.append(nums[i])
    return result


#Approach 2: Right to Left pass (optimal)
#Time: O(n)
def leaders_optimal(nums):
    n = len(nums)
    result = []
    max_from_right = float('-inf')

    for i in range(n-1, -1, -1):
        if nums[i] > max_from_right:
            result.append(nums[i])
            max_from_right = nums[i]
    return result[::-1]