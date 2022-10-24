#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        # find the highest digit
        highest = 1
        while n // highest >= 10:
            highest *= 10
        # find the number of 1s in the highest digit
        high = n // highest
        if high == 1:
            return self.countDigitOne(highest - 1) + n % highest + 1 + self.countDigitOne(n % highest)
        else:
            return highest + high * self.countDigitOne(highest - 1) + self.countDigitOne(n % highest)
# @lc code=end

