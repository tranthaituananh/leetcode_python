#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#

# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(31, -1, -1):
            res <<= 1
            prefix = {num >> i for num in nums}
            res += any(res ^ 1 ^ p in prefix for p in prefix)
        return res
# @lc code=end

