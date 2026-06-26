# ============================================================
# LeetCode 19 - Remove Nth Node From End of List
# ============================================================
# Given the head of a linked list, remove the nth node
# from the end of the list and return the head.
#
# Example:
#   Input:  1 -> 2 -> 3 -> 4 -> 5, n = 2
#   Output: 1 -> 2 -> 3 -> 5  (removed 4, the 2nd from end)
#
#   Input:  1, n = 1
#   Output: (empty)
#
#   Input:  1 -> 2, n = 1
#   Output: 1
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — Two Pointer approach
# ============================================================

#Approach 1: Two Pointer
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def nth_node_optimal(head, n):
    dummy = Node(-1)
    dummy.next = head
    slow = fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next
