#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(k, n, start, path, res):
            if k == 0 and n == 0:
                res.append(path)
                return
            for i in range(start, 10):
                if i > n:
                    break
                dfs(k-1, n-i, i+1, path+[i], res)
        res = []
        dfs(k, n, 1, [], res)
        return res
# @lc code=end

