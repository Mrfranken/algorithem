# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode(next=head)
        node = dummy_head
        while node.next:
            print(node.val)
            if node.next.val == val:
                node.next = node.next.next
            else:
                # print(node.val)
                node = node.next
        return dummy_head.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    solution = Solution()
    solution.removeElements(a, 3)
