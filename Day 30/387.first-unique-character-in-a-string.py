#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1])
# @lc code=end

