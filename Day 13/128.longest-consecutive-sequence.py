#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                cur = num
                while cur in nums:
                    cur += 1
                res = max(res, cur-num)
        return res
# @lc code=end

