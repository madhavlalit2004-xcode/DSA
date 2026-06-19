# ============================================================
# LeetCode 206 - Reverse Linked List
# ============================================================
# Given the head of a singly linked list, reverse the list
# and return the new head.
#
# Example:
#   Input:  1 -> 2 -> 3 -> 4 -> 5
#   Output: 5 -> 4 -> 3 -> 2 -> 1
#
#   Input:  1 -> 2
#   Output: 2 -> 1
#
#   Input:  (empty)
#   Output: (empty)
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — iterative approach
# ============================================================

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def reverse_ll_optimal(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev