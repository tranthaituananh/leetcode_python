#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        j = 1
        count = 1
        while j < len(nums):
            if nums[j] == nums[i]:
                count += 1
                if count <= 2:
                    i += 1
                    nums[i] = nums[j]
            else:
                count = 1
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1  
# @lc code=end

