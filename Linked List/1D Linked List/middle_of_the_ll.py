# ============================================================
# LeetCode 876 - Middle of the Linked List
# ============================================================
# Given the head of a singly linked list, return the middle node.
# If there are two middle nodes, return the second middle node.
#
# Example:
#   Input:  1 -> 2 -> 3 -> 4 -> 5
#   Output: 3  (middle node)
#
#   Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6
#   Output: 4  (second middle node for even length)
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — Slow & Fast Pointer
# ============================================================

#Approach 1: Count length
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def middle_node_count(head):
    length = 0
    current = head

    while current:
        lenght += 1
        current = current.next

    mid = length // 2
    current = head
    for _ in range(mid):
        current = current.next
    return current


#Approach 2: Slow and Fast Pointer:
def middle_node_count_optimal(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow