#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join('1' if x == '0' else '0' for x in bin(num)[2:]), 2)
# @lc code=end

