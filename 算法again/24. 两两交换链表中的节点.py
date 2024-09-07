# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    """
    1. 需要先定义一个预先的头节点，作为起始
    2. pre是左边的节点 cur是中间的节点 post是右边的节点
    3. 需要做的是交换cur和post的位置
        先把cur.next = post.next
        在单独把post.next = cur
        然后再把pre和post连起来 pre.next = post
        最后跳到交换的位置作为pre节点 pre = pre.next.next
    """
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(next=head)
        pre = dummy
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    s = Solution()
    print(s.swapPairs(l1))
