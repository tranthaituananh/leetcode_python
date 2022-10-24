#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [key for key, val in Counter(nums).items() if val > len(nums) // 3]
# @lc code=end

