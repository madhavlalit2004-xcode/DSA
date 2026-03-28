# ============================================================
# Print N to 1 Using Recursion
# ============================================================
# Given a number n, print all numbers from n down to 1
# using recursion — without any loops.
#
# Example:
#   Input:  n = 5
#   Output: 5 4 3 2 1
#
# Time Complexity:  O(n)  — n recursive calls
# Space Complexity: O(n)  — n frames on the call stack
# ============================================================

#Approach 1: Tail Recursion
def print_n_to_one(num):
    if num == 0:
        return
    print(num)
    print_n_to_one(num - 1)