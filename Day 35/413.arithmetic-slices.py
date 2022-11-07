#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        dp = [0] * len(nums)
        if nums[2] - nums[1] == nums[1] - nums[0]:
            dp[2] = 1
        for i in range(3, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)
# @lc code=end

