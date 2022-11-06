#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        res = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    res += max(0, h - heightMap[x][y])
                    heapq.heappush(heap, (max(h, heightMap[x][y]), x, y))
                    visited[x][y] = True
        return res
# @lc code=end
