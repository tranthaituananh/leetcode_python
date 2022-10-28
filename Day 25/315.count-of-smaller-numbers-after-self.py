#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        sorted_nums = []
        for i in range(n - 1, -1, -1):
            index = bisect.bisect_left(sorted_nums, nums[i])
            res[i] = index
            sorted_nums.insert(index, nums[i])
        return res
# @lc code=end

