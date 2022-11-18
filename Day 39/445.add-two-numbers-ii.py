#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(l):
            prev = None
            while l:
                next = l.next
                l.next = prev
                prev = l
                l = next
            return prev

        l1 = reverseList(l1)
        l2 = reverseList(l2)
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        return reverseList(dummy.next)
# @lc code=end

