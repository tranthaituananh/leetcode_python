#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)

    def gameOfLifeInfinite(self, live):
        neighbors = collections.Counter((I, J)
            for i, j in live
            for I in range(i-1, i+2)
            for J in range(j-1, j+2)
            if I != i or J != j)
        return {ij
            for ij in neighbors
            if neighbors[ij] == 3 or neighbors[ij] == 2 and ij in live}
# @lc code=end

