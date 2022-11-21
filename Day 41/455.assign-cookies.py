#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        for cookie in s:
            if res < len(g) and cookie >= g[res]:
                res += 1
        return res
# @lc code=end

