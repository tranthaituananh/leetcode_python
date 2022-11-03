#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input = input.split('\n')
        stack = []
        max_len = 0
        for line in input:
            tabs = line.count('\t')
            while len(stack) > tabs:
                stack.pop()
            stack.append(line.replace('\t', ''))
            if '.' in line:
                max_len = max(max_len, len('/'.join(stack)))
        return max_len
# @lc code=end
