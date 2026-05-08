# ============================================================
# Leetcode: 11 Container with most water
# ============================================================
# Given an integer array height where each element represents
# the height of a vertical line.
# Find two lines that together with the x-axis form a container
# such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Must run in O(n) time and O(1) space.
#
# Example:
#   Input:  height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
#
#   Input:  height = [1,1]
#   Output: 1
#
#   Input:  height = [4,3,2,1,4]
#   Output: 16
#
# Key Insight:
#   Area = min(height[left], height[right]) * (right - left)
#
#   The smaller height limits the water capacity.
#
#   If height[left] < height[right]:
#       → move left pointer
#
#   Else:
#       → move right pointer
#
#   Moving the taller pointer cannot increase area because
#   width decreases and smaller height still limits the area.
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Two Pointer
def container_with_most_water(height):
    left = 0
    right = len(height) - 1
    ans = 0

    while left < right:
        if height[left] < height[right]:
            ans = max(height[left]* (right-left), ans)
            left += 1
        else:
            ans = max(height[right] * (right - left), ans)
            right -= 1
    
    return ans