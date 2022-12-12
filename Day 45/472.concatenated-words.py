#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        def dfs(word):
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in words and suffix in words:
                    return True
                if prefix in words and dfs(suffix):
                    return True
            return False
        return [word for word in words if dfs(word)]
# @lc code=end

