#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    max_count = 0
    current_count = 0
    result = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if root.val == self.prev:
            self.current_count += 1
        else:
            self.current_count = 1
        if self.current_count > self.max_count:
            self.max_count = self.current_count
            self.result = [root.val]
        elif self.current_count == self.max_count:
            self.result.append(root.val)
        self.prev = root.val
        self.inorder(root.right)
# @lc code=end
