#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        edge = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                edge[word[:i] +'*'+word[i+1:]].add(word)
        queue = set()
        queue.add(beginWord)
        minl = 1
        while queue:
            next_queue = set()
            for word in queue:
                if word in wordList:
                    wordList.remove(word)
            for word in queue:
                if word == endWord:
                    return minl
                for i in range(len(word)):
                    for w in edge[word[:i]+'*'+word[i+1:]]:
                        if w in wordList:
                            next_queue.add(w)
            queue = next_queue
            minl += 1
        return 0
# @lc code=end

