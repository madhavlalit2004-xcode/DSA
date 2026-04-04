# ============================================================
# LeetCode 121 - Best Time to Buy and Sell Stock
# ============================================================
# Given an array prices where prices[i] is the price of a
# stock on day i, return the maximum profit you can achieve.
# You must buy before you sell. If no profit, return 0.
#
# Example:
#   Input:  prices = [7, 1, 5, 3, 6, 4]
#   Output: 5  (buy on day 2 at price 1, sell on day 5 at 6)
#
#   Input:  prices = [7, 6, 4, 3, 1]
#   Output: 0  (prices always fall — no profit possible)
#
#   Input:  prices = [1, 2]
#   Output: 1
#
# Time Complexity:  O(n)   — single pass
# Space Complexity: O(1)
# ============================================================

#Approach 1: Brute Force
#Time: O(n^2)
def max_profit_brute(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


#Approach 2: Kadanes Varient
#Time: O(n)
def max_profit_optimal(prices):
    max_profit = float('inf')
    bestBuy = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > bestBuy:
            max_profit = max(max_profit, prices[i] - bestBuy)
        bestBuy = min(bestBuy, prices[i])
    return max_profit