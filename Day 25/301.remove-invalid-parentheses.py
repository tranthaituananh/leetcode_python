#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        level = {s}
        while True:
            valid = list(filter(is_valid, level))
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}
# @lc code=end

