# ============================================================
# Insertion at the Head of Linked List
# ============================================================
# Given a linked list and a value, insert a new node with
# that value at the HEAD (beginning) of the list.
# Return the new head of the list.
#
# Example:
#   Input:  list = 1 -> 2 -> 3, value = 0
#   Output: 0 -> 1 -> 2 -> 3
#
#   Input:  list = (empty), value = 5
#   Output: 5
#
# Time Complexity:  O(1)
# Space Complexity: O(1)
# ============================================================

#Approach 1: 
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def insert_at_head_optimal(head, value):
        new_node = Node(value)
        new_node.next = head
        return new_node

    def print_list(head: None) -> None:
        elements = []
        current = head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "(empty)")