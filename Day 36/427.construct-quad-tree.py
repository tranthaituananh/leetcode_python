#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        if len(grid) == 1:
            return Node(grid[0][0], True, None, None, None, None)
        if all(grid[i][j] == grid[0][0] for i in range(len(grid)) for j in range(len(grid))):
            return Node(grid[0][0], True, None, None, None, None)
        n = len(grid) // 2
        return Node(
            True,
            False,
            self.construct([row[:n] for row in grid[:n]]),
            self.construct([row[n:] for row in grid[:n]]),
            self.construct([row[:n] for row in grid[n:]]),
            self.construct([row[n:] for row in grid[n:]])
        )
# @lc code=end

