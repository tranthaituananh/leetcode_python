#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [1, 1]
        for i in range(2, rowIndex + 1):
            res = [1] + [res[j] + res[j + 1] for j in range(i - 1)] + [1]
        return res
# @lc code=end

