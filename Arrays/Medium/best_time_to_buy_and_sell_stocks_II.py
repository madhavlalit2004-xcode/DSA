# ============================================================
# LeetCode 122 - Best Time to Buy and Sell Stock II
# ============================================================
# Given an array prices where prices[i] is the price of a
# stock on day i, return the maximum profit you can achieve.
# You may buy and sell on the same day.
# You may NOT hold more than one stock at a time.
# You CAN complete as many transactions as you like.
#
# Example:
#   Input:  prices = [7, 1, 5, 3, 6, 4]
#   Output: 7  (buy at 1 sell at 5 = 4, buy at 3 sell at 6 = 3 → total 7)
#
#   Input:  prices = [1, 2, 3, 4, 5]
#   Output: 4  (buy at 1, sell at 5)
#
#   Input:  prices = [7, 6, 4, 3, 1]
#   Output: 0  (prices always fall — no profit)
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ============================================================

#Approach 1: Optimal
def best_time_to_buy_stocks_II(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]:
            profit = profit + prices[i] - prices[i-1]
    return profit