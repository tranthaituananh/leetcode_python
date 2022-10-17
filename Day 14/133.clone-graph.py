#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        return self.dfs(node, {})

    def dfs(self, node, visited):
        if node in visited:
            return visited[node]
        clone = Node(node.val)
        visited[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(self.dfs(neighbor, visited))
        return clone
# @lc code=end

