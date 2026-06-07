# ============================================================
# Find the Missing and Repeating Number
# ============================================================
# Given an array of n integers where each number should appear
# exactly once in range [1, n], one number appears twice
# (repeating) and one number is missing. Find both.
#
# Example:
#   Input:  nums = [3, 1, 3]
#   Output: Repeating = 3, Missing = 2
#
#   Input:  nums = [1, 3, 2, 3, 4, 5]  (n=6)
#   Output: Repeating = 3, Missing = 6
#
#   Input:  nums = [4, 3, 6, 2, 1, 1]
#   Output: Repeating = 1, Missing = 5
#
# Time Complexity:  O(n)   — Math / XOR approach
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force
def find_missing_repeating_brute(nums):
    missing = -1
    repeating = -1
    for i in range(1, len(nums) + 1):
        count = 0
        for j in range(0, len(nums)):
            if nums[j] == i:
                count += 1
        if count == 2:
            repeating = i
        elif count == 0:
            missing = i
        
        if missing != -1 and repeating != -1:
            break
    
    return [missing, repeating]


#Approach 2: Sum Approach 
def find_miss_repeat_optimal(nums):
    n = len(nums)
    sn = (n * (n + 1)) / 2
    s2n = (n * (n + 1) * (2*n + 1)) / 6
    s = 0
    s2 = 0
    for i in range(0, n):
        s += nums[i]
        s2 += nums[i] * nums[i]

    val1 = s - sn
    val2 = s2 - s2n
    val2 = val2 / val1
    x = (val1 + val2) / 2
    y = x - val1
    return [int(x), int(y)]

print(find_miss_repeat_optimal([1, 2, 3, 6, 7, 5, 7]))