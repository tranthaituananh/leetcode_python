#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, seq):
            if not node:
                return
            seq.append(node.val)
            if not node.left and not node.right:
                self.res += int(''.join(map(str, seq)))
            dfs(node.left, seq)
            dfs(node.right, seq)
            seq.pop()
        self.res = 0
        dfs(root, [])
        return self.res
# @lc code=end

