# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverse(self, l):
        cur = l
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        jin_wei = 0

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        while l1 or l2:
            add1 = l1.val if l1 else 0
            add2 = l2.val if l2 else 0
            sum_value = add1 + add2 + jin_wei
            value = sum_value % 10
            jin_wei = sum_value // 10
            res.append(value)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if jin_wei:
            res.append(jin_wei)
        res = res[::-1]
        g = d = ListNode(res[0])
        for i in range(1, len(res)):
            d.next = ListNode(res[i])
            d = d.next
        return g


if __name__ == '__main__':
    l1 = [7, 2, 4, 3]
    i = 1
    d1 = g = ListNode(l1[0])
    while i < len(l1):
        g.next = ListNode(l1[i])
        g = g.next
        i += 1

    l2 = [5, 6, 4]
    i = 1
    d2 = g = ListNode(l2[0])
    while i < len(l2):
        g.next = ListNode(l2[i])
        g = g.next
        i += 1

    s = Solution()
    print(s.addTwoNumbers(d1, d2))
