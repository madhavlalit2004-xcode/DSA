# ============================================================
# Print 1 to N Using Recursion
# ============================================================
# Given a number n, print all numbers from 1 to n
# using recursion — without any loops.
#
# Example:
#   Input:  n = 5
#   Output: 1 2 3 4 5
#
# Time Complexity:  O(n)  — n recursive calls
# Space Complexity: O(n)  — n frames on the call stack
# ============================================================

#Approach1: Head Recursion
def print_one_to_n(num):
    if num == 0:
        return 
    print_one_to_n(num - 1)
    print(num)