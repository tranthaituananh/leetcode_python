#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        target = perimeter // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False
        sides = [0] * 4
        def dfs(idx):
            if idx == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == target
            for i in range(4):
                if sides[i] + matchsticks[idx] > target:
                    continue
                sides[i] += matchsticks[idx]
                if dfs(idx + 1):
                    return True
                sides[i] -= matchsticks[idx]
            return False
        return dfs(0)
# @lc code=end

