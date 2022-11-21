#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        res = 1
        end = points[0][1]
        for point in points:
            if point[0] > end:
                res += 1
                end = point[1]
        return res
# @lc code=end

