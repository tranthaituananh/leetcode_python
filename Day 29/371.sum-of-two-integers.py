#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > mask else a
# @lc code=end
