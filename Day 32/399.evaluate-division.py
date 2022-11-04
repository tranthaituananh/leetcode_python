#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v
        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(self.dfs(graph, a, b, set()))
        return res
        
    def dfs(self, graph, a, b, visited):
        if a == b:
            return 1.0
        visited.add(a)
        for c in graph[a]:
            if c not in visited:
                res = self.dfs(graph, c, b, visited)
                if res != -1.0:
                    return res * graph[a][c]
        return -1.0
# @lc code=end

