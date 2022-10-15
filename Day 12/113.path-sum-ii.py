#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]] if root.val == targetSum else []
        return [[root.val] + path for path in self.pathSum(root.left, targetSum - root.val)] + [[root.val] + path for path in self.pathSum(root.right, targetSum - root.val)]
# @lc code=end

