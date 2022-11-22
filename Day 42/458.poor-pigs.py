#
# @lc app=leetcode id=458 lang=python3
#
# [458] Poor Pigs
#

# @lc code=start
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
# @lc code=end

