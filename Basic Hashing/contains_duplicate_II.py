def contains_duplicate_optimal(nums, k):
    freq = {}
    for i, num in enumerate(nums):
        if num in freq and i - freq[num] <= k:
            return True
        freq[num] = i
    return False