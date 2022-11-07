#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        for i in range(m):
            self.dfs(heights, pacific, i, 0)
            self.dfs(heights, atlantic, i, n-1)
        for j in range(n):
            self.dfs(heights, pacific, 0, j)
            self.dfs(heights, atlantic, m-1, j)
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result 

    def dfs(self, heights, visited, i, j):
        m, n = len(heights), len(heights[0])
        if visited[i][j]:
            return
        visited[i][j] = True
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                self.dfs(heights, visited, x, y)
# @lc code=end

