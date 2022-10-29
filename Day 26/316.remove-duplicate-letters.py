#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return s
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and s.find(stack[-1], i) != -1:
                stack.pop()
            stack.append(c)
        return ''.join(stack)
# @lc code=end

