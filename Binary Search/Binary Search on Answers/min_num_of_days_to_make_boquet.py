# ============================================================
# LeetCode 1482 - Minimum Number of Days to Make m Bouquets
# ============================================================
# You are given an integer array bloomDay, an integer m, and an integer k.
#
# bloomDay[i] = day on which the i-th flower will bloom.
#
# To make 1 bouquet, you need k adjacent flowers that have bloomed.
# You need to make exactly m bouquets.
#
# Return the minimum number of days required to make m bouquets.
# If it is not possible, return -1.
#
# Example:
#   Input:  bloomDay = [1,10,3,10,2], m = 3, k = 1
#   Output: 3
#
#   Input:  bloomDay = [1,10,3,10,2], m = 3, k = 2
#   Output: -1
#
#   Input:  bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
#   Output: 12
#
# Approach (Brute Force):
# - Try each day from min(bloomDay) to max(bloomDay)
# - For each day, count how many bouquets can be formed
# - Return first day where bouquets >= m
#
# Time Complexity:  O(n * maxDay)
# Space Complexity: O(1)
#
# Approach (Optimal - Binary Search):
# - Search on days range [min(bloomDay), max(bloomDay)]
# - For each mid day:
#     count how many bouquets can be formed
# - If bouquets >= m → try smaller day
# - Else → increase day
#
# Time Complexity:  O(n * log(maxDay))
# Space Complexity: O(1)
# ============================================================


#Approach 1: brute Force
def min_days_brute(bloomDay, m, k):
    n = len(bloomDay)

    if m * k > n:
        return -1
    
    for day in range(min(bloomDay), max(bloomDay) + 1):
        bouquets = 0
        flowers = 0
        for i in bloomDay:
            if i <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0

        if bouquets >= m:
            return day
    return -1


#Approach 2: Binary Search (optimal)
def min_day_optimal(bloomDay, m, k):
    n = len(bloomDay)

    if m * k > n:
        return -1
    
    def countDay(day):
        flowers = 0
        bouquet = 0
        for i in bloomDay:
            if i <= day:
                flowers += 1
                if flowers == k:
                    bouquet += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquet >= m
    
    low, high = min(bloomDay), max(bloomDay)
    while low <= high:
        mid = (low + mid) // 2

        if countDay(mid):
            high = mid - 1
        else:
            low = mid + 1
    
    return low