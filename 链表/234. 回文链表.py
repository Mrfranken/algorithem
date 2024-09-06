# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        https://leetcode.cn/problems/palindrome-linked-list/solutions/37367/dong-hua-yan-shi-234-hui-wen-lian-biao-by-user7439/
        链表 双指针
        """
        stack = []
        if not head:
            return False
        if not head.next:
            return True
        while head:
            stack.append(head.val)
            head = head.next
        fast = len(stack) - 1
        slow = 0
        while slow < fast:
            if stack[slow] != stack[fast]:
                return False
            else:
                slow += 1
                fast -= 1
        return True



if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(0)
    c = ListNode(1)
    d = ListNode(4)
    e = ListNode(1)
    a.next = b
    b.next = c
    # c.next = d
    # d.next = e
    solution = Solution()
    print(solution.isPalindrome(a))
