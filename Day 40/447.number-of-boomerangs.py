#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p in points:
            cnt = collections.defaultdict(int)
            for q in points:
                cnt[(p[0]-q[0])**2 + (p[1]-q[1])**2] += 1
            for k in cnt:
                res += cnt[k] * (cnt[k]-1)
        return res
# @lc code=end

