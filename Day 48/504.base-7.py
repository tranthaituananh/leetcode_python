#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        result = []
        negative = num < 0
        num = abs(num)
        while num > 0:
            result.append(str(num % 7))
            num //= 7
        if negative:
            result.append('-')
        return ''.join(reversed(result))
# @lc code=end

