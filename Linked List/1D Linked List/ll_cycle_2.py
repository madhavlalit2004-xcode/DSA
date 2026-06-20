# ============================================================
# LeetCode 142 - Linked List Cycle II
# ============================================================
# Given the head of a linked list, return the node where the
# cycle begins. If there is no cycle, return None.
#
# Example:
#   Input:  3 -> 2 -> 0 -> -4 -> (back to 2)
#   Output: node with value 2  (cycle starts at index 1)
#
#   Input:  1 -> 2 -> (back to 1)
#   Output: node with value 1  (cycle starts at index 0)
#
#   Input:  1
#   Output: None  (no cycle)
#
# Key Insight (Floyd's Algorithm Extension):
#   After slow and fast meet inside the cycle:
#   Move one pointer back to head
#   Move both pointers one step at a time
#   They will meet exactly at the cycle start!
#
# Proof:
#   Let L = distance from head to cycle start
#   Let C = cycle length
#   When they meet: slow traveled L + a, fast traveled L + a + nC
#   Since fast = 2 * slow → L + a = nC → L = nC - a
#   So moving from head by L steps = moving from meeting point by nC - a steps
#   Both arrive at cycle start simultaneously!
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — Floyd's Algorithm
# ============================================================

#Approach 1: Floyd's Algorithm
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def find_cycle_optimal(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    
    slow = head
    if slow != fast:
        slow = slow.next
        fast = fast.next
    return slow