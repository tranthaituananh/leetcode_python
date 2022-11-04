#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        else:
            return min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1
# @lc code=end

