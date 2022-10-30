#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        top = -1
        preorder = preorder.split(',')
        for s in preorder:
            stack.append(s)
            top += 1
            while top >= 2 and stack[top] == '#' and stack[top-1] == '#' and stack[top-2] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                top -= 3
                stack.append('#')
                top += 1
        return top == 0 and stack[0] == '#'
# @lc code=end

