#
# @lc app=leetcode id=391 lang=python3
#
# [391] Perfect Rectangle
#

# @lc code=start
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corner_points = set()
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            corner_points ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
        if len(corner_points) != 4:
            return False
        x1, y1 = min(corner_points)
        x2, y2 = max(corner_points)
        return area == (x2 - x1) * (y2 - y1)
# @lc code=end

