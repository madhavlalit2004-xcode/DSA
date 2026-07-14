# ============================================================
# LeetCode 705 - Design HashSet
# ============================================================
# Design a HashSet without using any built-in hash table libraries.
# Implement the following:
#   - add(key)     → insert key into HashSet
#   - remove(key)  → remove key from HashSet if present
#   - contains(key) → return True if key exists, False otherwise
#
# Example:
#   myHashSet = MyHashSet()
#   myHashSet.add(1)
#   myHashSet.add(2)
#   myHashSet.contains(1) → True
#   myHashSet.contains(3) → False
#   myHashSet.add(2)
#   myHashSet.contains(2) → True
#   myHashSet.remove(2)
#   myHashSet.contains(2) → False
#
# Constraints: 0 <= key <= 10^6
#
# Time Complexity:  O(1) average — hashing
# Space Complexity: O(n)
# ============================================================
 
#Approach 1: 
class MyHashSet_array:
    def __init__(self):
        self.hashset = [False] * (10**6 + 1)

    def add(self, key):
        self.hashset[key] = True

    def remove(self, key):
        self.hashset[key] = False
    
    def contains(self, key):
        return self.hashset[key]