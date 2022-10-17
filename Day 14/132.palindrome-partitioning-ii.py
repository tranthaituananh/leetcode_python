#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [i for i in range(n)]
        for i in range(n):
            self.expand(s, i, i, dp)
            self.expand(s, i, i + 1, dp)
        return dp[-1]

    def expand(self, s, left, right, dp):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if left == 0:
                dp[right] = 0
            else:
                dp[right] = min(dp[right], dp[left - 1] + 1)
            left -= 1
            right += 1
# @lc code=end

