#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] > n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l
# @lc code=end

