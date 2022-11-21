#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import Counter
        counter = Counter()
        for num1 in nums1:
            for num2 in nums2:
                counter[num1 + num2] += 1
        res = 0
        for num3 in nums3:
            for num4 in nums4:
                res += counter[-num3 - num4]
        return res
# @lc code=end

