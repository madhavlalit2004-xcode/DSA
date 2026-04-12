# LeetCode 56 - Merge Intervals
# ============================================================
# Given an array of intervals where intervals[i] = [start, end],
# merge all overlapping intervals and return an array of the
# non-overlapping intervals that cover all the intervals.
#
# Example:
#   Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#
#   Input:  intervals = [[1,4],[4,5]]
#   Output: [[1,5]]   (touching intervals are merged)
#
#   Input:  intervals = [[1,4],[2,3]]
#   Output: [[1,4]]   (one fully contains the other)
#
# Time Complexity:  O(n log n)  — sorting dominates
# Space Complexity: O(n)        — result array
# ============================================================

#Approach 1: Sort + Linear Search (optimal)
#Sort by start time
#Compare each interval with last merged interval
#If overlapping -> extend the end, else -> add new interval
#Time: O(n log n)
def merge_optimal(intervals):
    intervals.sort()
    result = []

    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result

print(merge_optimal([[1, 3], [2, 6], [8, 10], [15, 18]]))