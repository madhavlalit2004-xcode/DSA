# ============================================================
# LeetCode 20 - Valid Parentheses
# ============================================================
# Given a string s containing just '(', ')', '{', '}', '[', ']',
# determine if the input string is valid.
# A string is valid if:
#   - Open brackets are closed by the same type of bracket
#   - Open brackets are closed in the correct order
#   - Every close bracket has a corresponding open bracket
#
# Example:
#   Input:  s = "()"
#   Output: True
#
#   Input:  s = "()[]{}"
#   Output: True
#
#   Input:  s = "(]"
#   Output: False
#
#   Input:  s = "([)]"
#   Output: False
#
#   Input:  s = "{[]}"
#   Output: True
#
# Time Complexity:  O(n)
# Space Complexity: O(n)  — stack
# ============================================================

#Approach 1: Stack (optimal)
def valid_parenthesis(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else "#"
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)
    return not stack