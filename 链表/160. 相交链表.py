# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/887414/xiang-jiao-lian-biao-wu-chong-jie-fa-by-j73p5/
        链表
        经验：
        1. 链表由一个个节点组成，这个节点是一个对象，即使是拥有同样value的node也不是同一个节点
        2. 不同链表可以使用同一个节点
        """
        a = headA
        b = headB
        s = set()
        while a:
            s.add(a)
            a = a.next
        while b:
            if b in s:
                return b
            else:
                b.next = b
        return None

