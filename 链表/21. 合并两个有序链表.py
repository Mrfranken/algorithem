# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 or not list2:
            return list1 if not list2 else list2

        d = {}
        while list1:
            if not d.get(list1.val, []):
                d[list1.val] = [list1]
            else:
                d[list1.val].append(list1)
            list1 = list1.next
        while list2:
            if not d.get(list2.val, []):
                d[list2.val] = [list2]
            else:
                d[list2.val].append(list2)
            list2 = list2.next

        d = dict(sorted(d.items(), key=lambda x: x[0]))

        dummpy = ListNode(0)
        dummpy_node = dummpy
        for _, key in d.items():
            for node in key:
                dummpy.next = node
                dummpy = dummpy.next

        return dummpy_node.next


if __name__ == '__main__':
    a = ListNode(-9)
    b = ListNode(3)
    # c = ListNode(4)
    d = ListNode(5)
    e = ListNode(7)
    # f = ListNode(4)
    a.next = b
    # b.next = c
    d.next = e
    # e.next = f
    solution = Solution()
    solution.mergeTwoLists(a, d)
