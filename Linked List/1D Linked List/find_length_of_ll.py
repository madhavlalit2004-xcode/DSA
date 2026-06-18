# ============================================================
# Find Length of a Linked List
# ============================================================
# Given the head of a singly linked list, return its length
# (number of nodes).
#
# Example:
#   Input:  head = 1 -> 2 -> 3 -> 4 -> None
#   Output: 4
#
# Approach (Iterative):
# - Traverse the linked list from head
# - Count each node until reaching None
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
#
# Approach (Recursive):
# - If head is None → return 0
# - Else return 1 + length of next node
#
# Time Complexity:  O(n)
# Space Complexity: O(n)  (recursion stack)
# ============================================================

#Approach 1:
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def count_element(self, head):
    count = 0
    temp = head

    while temp is not None:
        count += 1
        temp = temp.next

    return count