#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            j = abs(nums[i]) - 1
            nums[j] = -abs(nums[j])
        return [i+1 for i in range(n) if nums[i] > 0]
# @lc code=end

