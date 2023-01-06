#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(score, reverse=True)
        result = []
        for s in score:
            if rank.index(s) == 0:
                result.append('Gold Medal')
            elif rank.index(s) == 1:
                result.append('Silver Medal')
            elif rank.index(s) == 2:
                result.append('Bronze Medal')
            else:
                result.append(str(rank.index(s) + 1))
        return result
# @lc code=end

