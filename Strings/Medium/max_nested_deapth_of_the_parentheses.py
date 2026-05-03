# ============================================================
# LeetCode 1614 - Maximum Nesting Depth of the Parentheses
# ============================================================
# Given a valid parentheses string s (VPS), return the
# maximum nesting depth.
# The nesting depth is the maximum number of open parentheses
# at any point during traversal.
#
# Example:
#   Input:  s = "(1+(2*3)+((8)/4))+1"
#   Output: 3   (((8)/4) has depth 3)
#
#   Input:  s = "(1)+((2))+(((3)))"
#   Output: 3
#
#   Input:  s = "1+(2*3)/(2-1)"
#   Output: 1
#
# Time Complexity:  O(n)
# Space Complexity: O(1)  — counter approach
# ============================================================

#Approach 1: Stack Based
#Push on "(", pop on ")"
#Time: O(n)
def max_deapth_stack(s):
    stack = []
    max_deapth = 0

    for ch in s:
        if ch == '(':
            stack.append(ch)
            max_deapth = max(max_deapth, len(stack))
        elif ch == ')':
            stack.pop()
    
    return max_deapth


#Approach 2: Counter (optimal)
#Track current deapth with a counter
#Increment in '(', decrement in ')'
#Time: O(n)
def max_deapth_counter(s):
    deapth = 0
    max_deapth = 0

    for ch in s:
        if ch == '(':
            deapth += 1
            max_deapth = max(max_deapth, deapth)
        elif ch == ')':
            deapth -= 1
    return max_deapth