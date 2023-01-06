#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return 0
            tot = root.val+dfs(root.left)+dfs(root.right)
            res.append(tot)
            return tot
        dfs(root)
        count = {}
        res2 = []
        for i in res:
            count[i] = 1 + count.get(i, 0)
        maxi = max(count.values())
        for j in count:
            if count[j] == maxi:
                res2.append(j)
        return res2
# @lc code=end
