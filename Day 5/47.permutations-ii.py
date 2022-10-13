#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        counter = Counter(nums)
        def findAllPermutations(res):
            if len(res) == len(nums):
                permutations.append(res)
                return
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    findAllPermutations(res + [num])
                    counter[num] += 1
        findAllPermutations([])
        return permutations
# @lc code=end

