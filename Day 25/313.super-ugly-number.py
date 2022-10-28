#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1] * n
        idx = [0] * len(primes)
        for i in range(1, n):
            dp[i] = min(dp[idx[j]] * primes[j] for j in range(len(primes)))
            for j in range(len(primes)):
                if dp[i] == dp[idx[j]] * primes[j]:
                    idx[j] += 1
        return dp[n - 1]
# @lc code=end

