#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robRange(nums, 0, len(nums) - 2), self.robRange(nums, 1, len(nums) - 1))

    def robRange(self, nums, start, end):
        first = second = 0
        for i in range(start, end + 1):
            first, second = second, max(first + nums[i], second)
        return second
# @lc code=end

