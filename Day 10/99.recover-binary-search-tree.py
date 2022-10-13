#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.val > node.val:
                self.first = self.first or self.prev
                self.second = node
            self.prev = node
            inorder(node.right)
        self.first = None
        self.second = None
        self.prev = None
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
# @lc code=end

