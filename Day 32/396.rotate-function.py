#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        s = sum(nums)
        f = sum(i * nums[i] for i in range(n))
        res = f
        for i in range(1, n):
            f = f + s - n * nums[n - i]
            res = max(res, f)
        return res
# @lc code=end

