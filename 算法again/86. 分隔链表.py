# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    """
    双指针
    """

    def __init__(self):
        self.dummy_small = ListNode(None, None)
        self.dummy_big = ListNode(None, None)

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = self.dummy_small
        big = self.dummy_big
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        small.next = self.dummy_big.next
        big.next = None
        return self.dummy_small.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(5)
    f = ListNode(2)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    solution = Solution()
    solution.partition(a, 3)


