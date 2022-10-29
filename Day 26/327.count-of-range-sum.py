#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#

# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def merge_sort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            i = j = mid
            for left in sums[lo:mid]:
                while i < hi and sums[i] - left < lower:
                    i += 1
                while j < hi and sums[j] - left <= upper:
                    j += 1
                count += j - i
            sums[lo:hi] = sorted(sums[lo:hi])
            return count
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        return merge_sort(0, len(sums))
# @lc code=end

