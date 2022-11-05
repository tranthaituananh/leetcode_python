#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        if len(stones) == 2:
            return True
        dp = {stone: set() for stone in stones}
        dp[1].add(1)
        for stone in stones:
            for step in dp[stone]:
                for next_step in [step - 1, step, step + 1]:
                    if next_step > 0 and stone + next_step in dp:
                        dp[stone + next_step].add(next_step)
        return len(dp[stones[-1]]) > 0        
# @lc code=end

