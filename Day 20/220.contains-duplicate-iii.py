#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        buckets = {}
        for i, num in enumerate(nums):
            bucket = num // (valueDiff + 1)
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True
            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True
            buckets[bucket] = num
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // (valueDiff + 1)]
        return False
# @lc code=end

