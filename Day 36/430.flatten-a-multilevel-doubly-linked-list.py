#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        stack = [head]
        prev = None
        while stack:
            node = stack.pop()
            if prev:
                prev.next = node
                node.prev = prev
            prev = node
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None
        return head
# @lc code=end

