#
# @lc app=leetcode id=477 lang=python3
#
# [477] Total Hamming Distance
#

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            ans += count * (len(nums) - count)
        return ans
        
# @lc code=end

