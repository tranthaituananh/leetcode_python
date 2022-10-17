#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = head
        while node:
            new_node = Node(node.val, node.next)
            node.next = new_node
            node = new_node.next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        node = head
        new_head = head.next
        while node:
            new_node = node.next
            node.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            node = node.next
        return new_head
# @lc code=end

