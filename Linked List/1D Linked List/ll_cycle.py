# ============================================================
# LeetCode 141 - Linked List Cycle
# ============================================================
# Given the head of a linked list, determine if it has a cycle.
# A cycle exists if a node can be reached again by following
# the next pointers.
#
# Example:
#   Input:  3 -> 2 -> 0 -> -4 -> (back to 2)
#   Output: True
#
#   Input:  1 -> 2 -> (back to 1)
#   Output: True
#
#   Input:  1
#   Output: False
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — Floyd's Algorithm
# ============================================================

#Approach 1: 
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
def has_cycle_optimal(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False