#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.pathSumFrom(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def pathSumFrom(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return (1 if root.val == targetSum else 0) + self.pathSumFrom(root.left, targetSum - root.val) + self.pathSumFrom(root.right, targetSum - root.val)
# @lc code=end

