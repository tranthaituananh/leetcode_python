#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build graph
        graph = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            graph[c].append(p)

        # 2. DFS
        visited = [0] * numCourses
        for c in range(numCourses):
            if not self.dfs(graph, visited, c):
                return False
        return True

    def dfs(self, graph, visited, c):
        if visited[c] == -1:
            return False
        if visited[c] == 1:
            return True
        visited[c] = -1
        for p in graph[c]:
            if not self.dfs(graph, visited, p):
                return False
        visited[c] = 1
        return True
# @lc code=end

