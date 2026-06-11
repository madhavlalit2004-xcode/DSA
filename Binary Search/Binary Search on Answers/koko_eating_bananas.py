# ============================================================
# LeetCode 875 - Koko Eating Bananas
# ============================================================
# Koko loves bananas. There are n piles, where piles[i] represents
# the number of bananas in the i-th pile. Guards will return in h hours.
#
# Koko can choose a speed k (bananas/hour). Every hour, she picks a pile
# and eats k bananas. If the pile has less than k bananas, she eats all.
#
# Return the minimum integer k such that Koko can eat all bananas within h hours.
#
# Example:
#   Input:  piles = [3,6,7,11], h = 8
#   Output: 4
#
#   Input:  piles = [30,11,23,4,20], h = 5
#   Output: 30
#
#   Input:  piles = [30,11,23,4,20], h = 6
#   Output: 23
#
# Approach (Brute Force):
# - Try all speeds k from 1 to max(piles)
# - For each k, compute total hours needed:
#       hours += ceil(pile / k)
# - Return the smallest k such that hours <= h
#
# Time Complexity:  O(n * max(piles))
# Space Complexity: O(1)
#
# Approach (Optimal - Binary Search):
# - Binary search on k in range [1, max(piles)]
# - For each mid (k), compute total hours required
# - If hours <= h → try smaller k
# - Else → increase k
#
# Time Complexity:  O(n * log(max(piles)))
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force
def koko_eating_brute(piles, h):
    for k in range(1, max(piles) + 1):
        hours = 0
        for pile in piles:
            hours = (pile + k - 1) // k
        
        if hours <= h:
            return k
        

#Approach 2: Binary Search (optimal)
def koko_eating_optimal(piles, h):
    low, high = 1, max(piles)
    
    while low <= high:
        mid = (low + high) // 2
        
        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid
        
        if hours < h:
            high = mid - 1
        else:
            low = mid + 1
    
    return low