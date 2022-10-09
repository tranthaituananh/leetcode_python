#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        result = 0
        for i in range(len(nums)):
            if i > result:
                return False
            result = max(result, i + nums[i])
        return True
# @lc code=end

