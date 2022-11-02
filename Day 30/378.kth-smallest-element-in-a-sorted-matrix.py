#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)

        def less_k(m):
            cnt = 0  # count
            for r in range(N):
                # binary search
                x = bisect_right(matrix[r], m)
                cnt += x
            return cnt

        while l < r:
            mid = (l+r) // 2

            if less_k(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l
# @lc code=end
