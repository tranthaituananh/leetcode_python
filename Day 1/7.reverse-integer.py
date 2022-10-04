#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        return res if res <= 0x7fffffff else 0
# @lc code=end

