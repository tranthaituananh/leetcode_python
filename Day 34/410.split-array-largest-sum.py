#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mid):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > mid:
                    count += 1
                    total = num
            return count <= k

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
# @lc code=end

