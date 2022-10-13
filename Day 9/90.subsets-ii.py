#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums, start, path):
        self.res.append(path)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]])
# @lc code=end

