# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        dummy = ListNode(next=head)
        while head:
            head = head.next
            count += 1

        cur = dummy
        for _ in range(count - n):
            cur = cur.next

        cur.next = cur.next.next
        return dummy.next