# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
        链表
        链表进行赋值时，对等号左值的改变会影响到右值
        """
        if not head:
            return head
        pre, cur = head, head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head
