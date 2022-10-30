#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        while len(res) <= n:
            res += [i+1 for i in res]
        return res[:n+1]
# @lc code=end

