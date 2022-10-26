#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res, self.target = [], target
        self.dfs(num, 0, 0, 0, '', res)
        return res

    def dfs(self, num, pos, prev, cur, path, res):
        if pos == len(num):
            if cur == self.target:
                res.append(path)
            return
        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0':
                break
            val = int(num[pos:i + 1])
            if pos == 0:
                self.dfs(num, i + 1, val, val, path + str(val), res)
            else:
                self.dfs(num, i + 1, val, cur + val, path + '+' + str(val), res)
                self.dfs(num, i + 1, -val, cur - val, path + '-' + str(val), res)
                self.dfs(num, i + 1, prev * val, cur - prev + prev * val, path + '*' + str(val), res)
# @lc code=end

