#
# @lc app=leetcode id=466 lang=python3
#
# [466] Count The Repetitions
#

# @lc code=start
class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if any(c for c in set(s2) if c not in set(s1)):
            return 0
        s2_index_to_reps = {0: (0, 0)}
        i, j = 0, 0
        s1_reps, s2_reps = 0, 0
        while s1_reps < n1:
            if s1[i] == s2[j]:
                j += 1
            i += 1
            if j == len(s2):
                j = 0
                s2_reps += 1
            if i == len(s1):
                i = 0
                s1_reps += 1
                if j in s2_index_to_reps:
                    break
                s2_index_to_reps[j] = (s1_reps, s2_reps)
        if s1_reps == n1:
            return s2_reps // n2
        initial_s1_reps, initial_s2_reps = s2_index_to_reps[j]
        loop_s1_reps = s1_reps - initial_s1_reps
        loop_s2_reps = s2_reps - initial_s2_reps
        loops = (n1 - initial_s1_reps) // loop_s1_reps
        s2_reps = initial_s2_reps + loops * loop_s2_reps
        s1_reps = initial_s1_reps + loops * loop_s1_reps
        while s1_reps < n1:
            if s1[i] == s2[j]:
                j += 1
            i += 1
            if i == len(s1):
                i = 0
                s1_reps += 1
            if j == len(s2):
                j = 0
                s2_reps += 1
        return s2_reps // n2
# @lc code=end
