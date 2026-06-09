# ============================================================
# Count Number of Substrings with Exactly K Distinct Characters
# ============================================================
# You are given a string s and a positive integer k.
# Return the number of substrings that contain exactly k distinct characters.
#
# Example:
#   Input:  s = "pqpqs", k = 2
#   Output: 7
#   Explanation: ["pq","pqp","pqpq","qp","qpq","pq","qs"]
#
#   Input:  s = "aabacbebebe", k = 3
#   Output: 7
#
# Approach (Brute Force):
# - Generate all substrings
# - For each substring, count distinct characters using a set
# - If distinct count == k, increment answer
#
# Time Complexity:  O(n^2 * k)
# Space Complexity: O(k)
#
# Approach (Optimal):
# - Use Sliding Window + HashMap
# - Count substrings with at most k distinct characters
# - Count substrings with at most (k-1) distinct characters
# - Answer = atMost(k) - atMost(k-1)
#
# Time Complexity:  O(n)
# Space Complexity: O(k)
# ============================================================

#Approach 1: Brute Force
def count_substring(s, k):
    n = len(s)
    count = 0
    for i in range(n):
        distinct = set()
        for j in range(i, n):
            distinct.add(s[j])
            if len(distinct) == k:
                count += 1
            elif len(distinct) > k:
                break
    return count

print(count_substring("pqpqs", 2))


#Approach 2: Sliding Window + Hashmap
def count_substring_optimal(s, k):
    def atmostk(self, s, k):
        freq = {}
        left = 0
        count = 0

        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            count += (right - left + 1)
        
        return count

    def count_substring(self, s, k):
        return self.atmostk(s, k) - self.atmostk(s, k-1)