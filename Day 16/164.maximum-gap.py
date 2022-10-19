#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        min_num, max_num = min(nums), max(nums)
        bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
        bucket_num = (max_num - min_num) // bucket_size + 1
        buckets = [[] for _ in range(bucket_num)]
        for num in nums:
            buckets[(num - min_num) // bucket_size].append(num)
        result, prev_max = 0, min_num
        for bucket in buckets:
            if not bucket:
                continue
            result = max(result, min(bucket) - prev_max)
            prev_max = max(bucket)
        return result
# @lc code=end

