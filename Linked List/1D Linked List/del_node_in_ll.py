# ============================================================
# LeetCode 237 - Delete Node in a Linked List
# ============================================================
# There is a singly-linked list, and you are given a node in the list
# (not the tail). Delete the given node. You are not given access to
# the head of the list.
#
# Example:
#   Input:  head = [4,5,1,9], node = 5
#   Output: [4,1,9]
#
#   Input:  head = [4,5,1,9], node = 1
#   Output: [4,5,9]
#
# Approach:
# - We cannot access the previous node, so we cannot delete directly
# - Copy the value of the next node into current node
# - Then skip the next node (node.next = node.next.next)
#
# Time Complexity:  O(1)
# Space Complexity: O(1)
# ============================================================

#Approach 1:
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def del_node(self, node):
        node.val = node.val.next
        node.next = node.next.next