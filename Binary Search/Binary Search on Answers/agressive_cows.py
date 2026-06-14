# ============================================================
# Aggressive Cows
# ============================================================
# Given an array of stall positions and an integer k (cows),
# place k cows in stalls such that the minimum distance
# between any two cows is MAXIMIZED.
# Return that maximum minimum distance.
#
# Example:
#   Input:  stalls = [1, 2, 4, 8, 9], k = 3
#   Output: 3
#   Explanation: place cows at 1, 4, 8 → min distance = 3
#
#   Input:  stalls = [1, 2, 3, 4, 5], k = 2
#   Output: 4
#   Explanation: place cows at 1, 5 → min distance = 4
#
# Key Insight:
#   Binary search on the ANSWER (the minimum distance)
#   Min possible distance = 1
#   Max possible distance = max(stalls) - min(stalls)
#   For a given distance d, greedily check if k cows can be placed
#   such that consecutive cows are at least d apart
#
# Time Complexity:  O(n log n + n * log(max-min))
# Space Complexity: O(1)
# ============================================================

#Approach 1: Binary Search (optimal)
def agressive_cows_optimal(stalls, k):
    def canPlaceCows(stalls, k, distance):
        count = 1
        last_position = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= distance:
                count += 1
                last_position = stalls[i]
                if count >= k:
                    return True
        return False
    
    stalls.sort()
    low, high = 1, max(stalls) - min(stalls)
    ans = 0

    while low <= high:
        mid = low + (high - low) // 2
        if canPlaceCows(stalls, k, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans