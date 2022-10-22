#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        res = []

        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        ref = set()
        for i in range(m):
            for j in range(n-1):
                ref.add(board[i][j] + board[i][j+1])
        for j in range(n):
            for i in range(m-1):
                ref.add(board[i][j] + board[i+1][j])

        for word in words:
            f = True
            for i in range(len(word)-1):
                if word[i:i+2] not in ref and word[i+1] + word[i] not in ref:
                    f = False
                    break
            if not f:
                continue
            if self.findWord(word, m, n, board, d):
                res.append(word)
        return res

    def findWord(self, word, m, n, board, d) -> bool:
        if word[:4] == word[0] * 4:
            word = ''.join([c for c in reversed(word)])
        starts = []
        stack = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    starts.append((i, j))
        for start in starts:
            stack.append(start)
            visited.add((start, ))
            l = 1
            while stack != [] and l < len(word):
                x, y = stack[-1]
                for dxy in d:
                    nx, ny = x + dxy[0], y + dxy[1]
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == word[l]:
                            if (nx, ny) not in stack and tuple(stack) + ((nx, ny),) not in visited:
                                stack.append((nx, ny))
                                visited.add(tuple(stack))
                                l += 1
                                if l == len(word):
                                    return True
                                break
                else:
                    stack.pop()
                    l -= 1
        else:
            return False  
# @lc code=end

