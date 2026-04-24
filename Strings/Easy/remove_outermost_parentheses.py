# ============================================================
# LeetCode 1021 - Remove Outermost Parentheses
# ============================================================
# A valid parentheses string is primitive if it is non-empty
# and cannot be split into two non-empty valid strings.
# Given a valid parentheses string s, remove the outermost
# parentheses of every primitive part and return the result.
#
# Example:
#   Input:  s = "(()())(())"
#   Output: "()()()"
#   Explanation: primitives are "(()())" and "(())"
#                after removing outermost: "()()" + "()" = "()()()"
#
#   Input:  s = "(()())(())(()(()))"
#   Output: "()()()()(())"
#
#   Input:  s = "()()"
#   Output: ""
#
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================================

#Approach 1: Count (optimal)
#Time: O(n)
def remove_outer_optimal(s):
    result = []
    count = 0

    for ch in s:
        if ch == '(':
            if count > 0:
                result.append(ch)
            count += 1
        else:
            count -= 1
            if count > 0:
                result.append(ch)
    return ''.join(result)