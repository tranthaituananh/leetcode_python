#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        res = [1] * n
        res[0] = res[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if res[i] == 1:
                res[i*i:n:i] = [0] * len(res[i*i:n:i])
        return sum(res)
# @lc code=end

