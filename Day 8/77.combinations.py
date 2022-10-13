#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(start, n + 1):
                dfs(i + 1, path + [i])
        res = []
        dfs(1, [])
        return res
# @lc code=end

