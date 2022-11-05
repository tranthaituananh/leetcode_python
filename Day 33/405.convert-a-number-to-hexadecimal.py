#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num += 2 ** 32
        res = ''
        while num:
            res = '0123456789abcdef'[num % 16] + res
            num //= 16
        return res
# @lc code=end

