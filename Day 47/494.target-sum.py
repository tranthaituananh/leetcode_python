#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(nums, target, i, memo):
            if i == len(nums):
                return 1 if target == 0 else 0
            if (i, target) in memo:
                return memo[(i, target)]
            memo[(i, target)] = dfs(nums, target - nums[i], i + 1, memo) + dfs(nums, target + nums[i], i + 1, memo)
            return memo[(i, target)]
        return dfs(nums, target, 0, {})
# @lc code=end

