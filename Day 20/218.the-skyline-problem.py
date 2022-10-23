#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        x_height_right_tuples = sorted(
            [(L, -H, R) for L, R, H in buildings] + [(R, 0, "doesn't matter") for _, R, _ in buildings])
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for x, height, right in x_height_right_tuples:
            while x >= live[0][1]:
                heapq.heappop(live)
            if height < 0:
                heapq.heappush(live, (height, right))
            if res[-1][1] != -live[0][0]:
                res.append([x, -live[0][0]])
        return res[1:]
# @lc code=end

