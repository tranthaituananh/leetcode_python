#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums) - 1:
            return 1
        if nums[0] == 0:
            return -1
        step = 1
        max_pos = nums[0]
        cur_pos = 0
        while max_pos < len(nums) - 1:
            step += 1
            cur_max = max_pos
            for i in range(cur_pos, max_pos + 1):
                cur_max = max(cur_max, i + nums[i])
            cur_pos = max_pos
            max_pos = cur_max
        return step
# @lc code=end

