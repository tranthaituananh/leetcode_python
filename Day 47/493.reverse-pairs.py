#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums, start, end):
            if start >= end:
                return 0
            mid = (start + end) // 2
            count = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end)
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            nums[start:end + 1] = sorted(nums[start:end + 1])
            return count
        return mergeSort(nums, 0, len(nums) - 1)
# @lc code=end

