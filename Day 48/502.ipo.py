#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        available = []
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(available, -projects[i][1])
                i += 1
            if available:
                w -= heapq.heappop(available)
            else:
                break
        return w
# @lc code=end
