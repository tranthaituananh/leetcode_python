#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        a = b = float('inf')
        for n in nums:
            if n <= a:
                a = n
            elif n <= b:
                b = n
            else:
                return True
        return False
# @lc code=end

