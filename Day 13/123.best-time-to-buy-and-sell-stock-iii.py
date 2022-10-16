#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        max_profit_left = [0] * len(prices)
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            max_profit_left[i] = max_profit
        max_profit = 0
        max_price = prices[-1]
        max_profit_right = [0] * len(prices)
        for i in range(len(prices) - 2, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])
            max_profit_right[i] = max_profit
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, max_profit_left[i] + max_profit_right[i])
        return max_profit
# @lc code=end

