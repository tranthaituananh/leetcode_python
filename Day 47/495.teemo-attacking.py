#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        res = 0
        for i in range(len(timeSeries) - 1):
            res += min(timeSeries[i + 1] - timeSeries[i], duration)
        return res + duration
# @lc code=end

