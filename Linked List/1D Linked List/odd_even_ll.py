# ============================================================
# LeetCode 328 - Odd Even Linked List
# ============================================================
# Given the head of a singly linked list, group all nodes
# with odd indices together followed by nodes with even indices.
# Note: indices start from 1 (1-indexed), not node values.
# The relative order within odd and even groups must be preserved.
#
# Example:
#   Input:  1 -> 2 -> 3 -> 4 -> 5
#   Output: 1 -> 3 -> 5 -> 2 -> 4
#
#   Input:  2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
#   Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — in-place
# ============================================================

#Approach:
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def odd_even_ll(head):
    if not head or not head.next:
        return head
    
    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.even = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head