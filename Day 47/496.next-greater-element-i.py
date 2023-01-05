#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            idx = nums2.index(i)
            for j in nums2[idx:]:
                if j > i:
                    res.append(j)
                    break
            else:
                res.append(-1)
        return res
# @lc code=end

