#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        if root.left:
            root.left.next = root.right or self.find_next(root.next)
        if root.right:
            root.right.next = self.find_next(root.next)
        self.connect(root.right)
        self.connect(root.left)
        return root

    def find_next(self, node):
        while node:
            if node.left:
                return node.left
            if node.right:
                return node.right
            node = node.next
        return None
# @lc code=end

