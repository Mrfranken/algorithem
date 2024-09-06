class MyQueue(object):
    """
    https://leetcode.cn/problems/implement-queue-using-stacks/description/
    栈
    栈栈模拟队列
    栈：  先进后出
    队列：先进先出
    """
    def __init__(self):
        self.sort_list = []
        self.reverse_list = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        for _ in range(len(self.reverse_list)):
            self.sort_list.append(self.reverse_list.pop())

        self.sort_list.append(x)
        for _ in range(len(self.sort_list)):
            self.reverse_list.append(self.sort_list.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.reverse_list.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.reverse_list[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.reverse_list) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
