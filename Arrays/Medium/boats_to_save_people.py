# ============================================================
# LeetCode 881 - Boats to Save People
# ============================================================
# Each boat carries at most 2 people, with a weight limit.
# Given array people and integer limit, return the minimum
# number of boats to carry everyone.
#
# Example:
#   Input:  people = [1, 2], limit = 3
#   Output: 1   (both fit in one boat: 1+2=3)
#
#   Input:  people = [3, 2, 2, 1], limit = 3
#   Output: 3   (boats: [1,2], [2], [3])
#
#   Input:  people = [3, 5, 3, 4], limit = 5
#   Output: 4   (boats: [3], [5], [3], [4] — no two fit together)
#
# Key Insight:
#   Sort + Two Pointer greedy:
#   Always try to pair the heaviest person with the lightest
#   If they fit → one boat for both, advance both pointers
#   If not → heaviest person goes alone, advance right only
#
# Time Complexity:  O(n log n)  — sorting dominates
# Space Complexity: O(1)
# ============================================================


#approach 1: Sort + Two Pointer (optimal)
def boats_to_save_people_optimal(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    
    return boats