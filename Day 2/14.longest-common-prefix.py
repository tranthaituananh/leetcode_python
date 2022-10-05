#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        res = strs[0]
        for s in strs:
            while not s.startswith(res):
                res = res[:-1]
        return res
# @lc code=end

