#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Build graph
        graph = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            graph[c].append(p)

        # 2. DFS
        visited = [0] * numCourses
        res = []
        for c in range(numCourses):
            if not self.dfs(graph, visited, c, res):
                return []
        return res

    def dfs(self, graph, visited, c, res):
        if visited[c] == -1:
            return False
        if visited[c] == 1:
            return True
        visited[c] = -1
        for p in graph[c]:
            if not self.dfs(graph, visited, p, res):
                return False
        visited[c] = 1
        res.append(c)
        return True
# @lc code=end

