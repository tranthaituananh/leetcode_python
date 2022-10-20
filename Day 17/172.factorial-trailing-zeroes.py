#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n > 0:
            n //= 5
            result += n
        return result        
# @lc code=end

