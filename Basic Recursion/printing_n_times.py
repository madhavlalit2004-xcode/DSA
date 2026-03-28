# ============================================================
# Print Something N Times Using Recursion
# ============================================================
# Given a number n and a message, print the message n times
# using recursion — without any loops.
#
# Example:
#   Input:  n = 5, message = "Hello"
#   Output:
#     Hello
#     Hello
#     Hello
#     Hello
#     Hello
#
# Time Complexity:  O(n)  — n recursive calls
# Space Complexity: O(n)  — n frames on the call stack
# ============================================================

#Approach 1: Head Recursion(Print before recursive call)
def print_head(num, message):
    if num == 0:
        return 
    print(message)
    print_head(num - 1, message)


#approach 2: Tail Recursion(recursive call before Print)
def tail_print(num, message):
    if num == 0:
        return 
    tail_print(num-1, message)
    print(message)