# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def trainingPlan(self, head, cnt):
        """
        :type head: Optional[ListNode]
        :type cnt: int
        :rtype: Optional[ListNode]https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solutions/702028/jian-zhi-offer-22-lian-biao-zhong-dao-sh-7u6x/
        链表
        """
        fast, slow = head, head
        for _ in range(cnt):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val
