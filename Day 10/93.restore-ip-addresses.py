#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, [], res)
        return res
    
    def dfs(self, s, index, path, res):
        if len(path) == 4 and index == len(s):
            res.append(".".join(path))
            return
        if len(path) == 4 and index != len(s):
            return
        for i in range(1, 4):
            if index + i > len(s):
                break
            if i != 1 and s[index] == "0":
                break
            if int(s[index:index + i]) > 255:
                break
            self.dfs(s, index + i, path + [s[index:index + i]], res)
# @lc code=end

