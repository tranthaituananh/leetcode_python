#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0
        for num in nums:
            if num == 1:
                current_ones += 1
            else:
                max_ones = max(max_ones, current_ones)
                current_ones = 0
        return max(max_ones, current_ones)
# @lc code=end

