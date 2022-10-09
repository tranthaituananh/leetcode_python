#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            result = max(result, nums[i])
        return result

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            result = max(result, nums[i])
        return result
# @lc code=end

