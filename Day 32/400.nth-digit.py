#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        n -= 10
        i = 2
        while n >= 9 * i * 10 ** (i - 1):
            n -= 9 * i * 10 ** (i - 1)
            i += 1
        num = 10 ** (i - 1) + n // i
        return int(str(num)[n % i])
# @lc code=end

