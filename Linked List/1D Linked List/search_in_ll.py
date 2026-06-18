# ============================================================
# Search in a Linked List
# ============================================================
# Given the head of a singly linked list and a target value,
# return True if the value exists in the list, otherwise False.
#
# Example:
#   Input:  head = 1 -> 2 -> 3 -> 4, target = 3
#   Output: True
#
#   Input:  head = 1 -> 2 -> 3 -> 4, target = 5
#   Output: False
#
# Approach (Iterative):
# - Traverse the linked list from head
# - Compare each node's value with target
# - If found → return True
# - If end reached → return False
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
#
# Approach (Recursive):
# - If head is None → return False
# - If head.data == target → return True
# - Else search in next node
#
# Time Complexity:  O(n)
# Space Complexity: O(n) (recursion stack)
# ============================================================

#Approach 1:
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def search_data(head, key):
    temp = head

    while temp is not None:
        if temp.data == key:
            return True
        temp = temp.next
    return False