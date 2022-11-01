#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopers = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopers)
        size = 0
        for enveloper in envelopers:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if dp[m] < enveloper[1]:
                    i = m + 1
                else:
                    j = m
            dp[i] = enveloper[1]
            size = max(i + 1, size)
        return size
# @lc code=end

