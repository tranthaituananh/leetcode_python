#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        state = [-1] * n
        result = []
        self.dfs(state, 0, result)
        return result

    def dfs(self, state, row, result):
        if row == len(state):
            result.append(self.draw(state))
            return
        for col in range(len(state)):
            if self.isValid(state, row, col):
                state[row] = col
                self.dfs(state, row + 1, result)
    
    def isValid(self, state, row, col):
        for i in range(row):
            if state[i] == col or abs(state[i] - col) == row - i:
                return False
        return True
    
    def draw(self, state):
        result = []
        for i in range(len(state)):
            row = ['.'] * len(state)
            row[state[i]] = 'Q'
            result.append(''.join(row))
        return result
# @lc code=end

