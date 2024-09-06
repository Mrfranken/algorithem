# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        if not head:
            return head
        count = 0
        while fast:
            fast = fast.next
            count += 1
        target = count // 2 + 1
        count = 1
        while head:
            head = head.next
            count += 1
            if target == count:
                return head


