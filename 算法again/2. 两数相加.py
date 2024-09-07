# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverse(self, x):
        cur = x
        next = None

        while cur:
            tmp = cur.next
            cur.next = next
            next = cur
            cur = tmp
        return next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_r = self.reverse(l1)
        l2_r = self.reverse(l2)
        carry = 0
        res = []
        while l1_r or l2_r or carry:
            num1 = l1_r.val if l1_r else 0
            num2 = l2_r.val if l2_r else 0
            sum_num = num1 + num2 + carry
            carry = sum_num // 10
            res.append(sum_num % 10)

            l1_r = l1_r.next if l1_r else None
            l2_r = l2_r.next if l2_r else None

        # res = res[::-1]

        dummy_node = ListNode()
        tmp = dummy_node

        for num in res:
            tmp.next = ListNode(val=num)
            tmp = tmp.next
        return dummy_node.next