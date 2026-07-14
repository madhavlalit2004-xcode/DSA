# ============================================================
# LeetCode 706 - Design HashMap
# ============================================================
# Design a HashMap without using any built-in hash table libraries.
# Implement the following:
#   - put(key, value)  → insert or update key-value pair
#   - get(key)         → return value if key exists, else -1
#   - remove(key)      → remove key if it exists
#
# Example:
#   myMap = MyHashMap()
#   myMap.put(1, 1)
#   myMap.put(2, 2)
#   myMap.get(1)    → 1
#   myMap.get(3)    → -1  (not found)
#   myMap.put(2, 1) → update value
#   myMap.get(2)    → 1
#   myMap.remove(2)
#   myMap.get(2)    → -1
#
# Constraints: 0 <= key, value <= 10^6
#
# Time Complexity:  O(1) average
# Space Complexity: O(n)
# ============================================================

#Approach 1:
class MyHashMap_array:
    def __init__(self):
        self.hashmap = [-1] * (10**6 + 1)

    def put(self, key, value):
        self.hashmap[key] = value

    def get(self, key):
        return self.hashmap[key]
    
    def remove(self, key):
        self.data[key] = -1