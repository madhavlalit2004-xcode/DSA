# ============================================================
# LeetCode 234 - Palindrome Linked List
# ============================================================
# Given the head of a singly linked list, return True if
# it is a palindrome, False otherwise.
#
# Example:
#   Input:  1 -> 2 -> 2 -> 1
#   Output: True
#
#   Input:  1 -> 2
#   Output: False
#
#   Input:  1 -> 2 -> 3 -> 2 -> 1
#   Output: True
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — optimal approach
# ============================================================

#Approach 1:
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def is_palindrome_optimal(head):
    if not head or not head.next:
        return True
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    second_half = prev

    first = head
    second = second_half
    result = True
    while second:
        if first.data != second.data:
            result = False
            break
        first = first.next
        second = second.next

    prev = None
    curr = second_half
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return result