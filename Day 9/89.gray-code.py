#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(2 ** n)]
# @lc code=end

