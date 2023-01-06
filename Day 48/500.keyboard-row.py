#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for word in words:
            for row in rows:
                if all(c in row for c in word.lower()):
                    res.append(word)
                    break
        return res
# @lc code=end
