#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        a, b = 2, 3
        for i in range(4, n+1):
            a, b = b, a + b
        return b
# @lc code=end
