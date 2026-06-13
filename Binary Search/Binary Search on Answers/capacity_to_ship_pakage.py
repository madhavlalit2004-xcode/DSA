# ============================================================
# LeetCode 1011 - Capacity to Ship Packages Within D Days
# ============================================================
# A conveyor belt has packages with weights[i].
# Ship all packages within days days.
# Packages must be shipped in order (cannot reorder).
# Find the minimum weight capacity of the ship.
#
# Example:
#   Input:  weights = [1,2,3,4,5,6,7,8,9,10], days = 5
#   Output: 15
#
#   Input:  weights = [3,2,2,4,1,4], days = 3
#   Output: 6
#
#   Input:  weights = [1,2,3,1,1], days = 4
#   Output: 3
#
# Key Insight:
#   Min capacity = max(weights)  → at least carry heaviest package
#   Max capacity = sum(weights)  → carry all in one day
#   Binary search between these two bounds
#
# Time Complexity:  O(n * log(sum - max))
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force (Linear Search)
def ship_capacity_brute(weights, days):
    def can_ship(weights, day, capacity):
        current_load = 0
        days_needed = 1

        for w in weights:
            if current_load + w > capacity:
                days_needed += 1
                current_load = 0
            current_load += w
        
        return days_needed <= days
    
    for capacity in range(max(weights), sum(weights)):
        if can_ship(weights, days, capacity):
            return capacity
    return sum(weights)


#Approach 2: Binary Search (optimal)
def ship_capacity(weights, days):
    def can_ship(weights, days, capacity):
        current_load = 0
        days_needed = 1

        for w in weights:
            if current_load + w > capacity:
                days_needed += 1
                current_load = 0
            current_load += w
        
        return days_needed <= days
    
    left = max(weights)
    right = sum(weights)
    ans = right
    
    while left <= right:
        mid = left - (right - left) // 2
        if can_ship(weights, days, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans