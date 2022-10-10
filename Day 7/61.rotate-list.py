#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        if k == 0:
            return head

        # get length of list
        length = 1
        node = head
        while node.next:
            length += 1
            node = node.next

        # get new head
        node.next = head
        k = k % length
        k = length - k
        while k > 0:
            node = node.next
            k -= 1
        new_head = node.next
        node.next = None

        return new_head
# @lc code=end

