#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            tmp_max = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmp_max)
                tmp_max = max(tmp_max, dp[i - 1][j - 1] - prices[j])
        return dp[-1][-1]
# @lc code=end

