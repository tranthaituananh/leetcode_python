#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                pre = dummy
                while pre.next.val <= cur.next.val:
                    pre = pre.next
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
        return dummy.next
# @lc code=end

