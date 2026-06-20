# ============================================================
# Length of Loop in Linked List
# ============================================================
# Given a linked list, find the length of the loop (cycle)
# if it exists. If no loop exists, return 0.
#
# Example:
#   Input:  1 -> 2 -> 3 -> 4 -> 5 -> (back to 3)
#   Output: 3  (loop: 3 -> 4 -> 5 -> back to 3)
#
#   Input:  1 -> 2 -> 3 -> 4 -> (back to 1)
#   Output: 4  (entire list is a loop)
#
#   Input:  1 -> 2 -> 3
#   Output: 0  (no loop)
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — Floyd's Algorithm
# ============================================================

#Approach 1: Floyd's Algo
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def length_of_loop_optimal(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    
    count  = 1
    fast = fast.next
    while fast != slow:
        count += 1
        fast = fast.next
    return count
