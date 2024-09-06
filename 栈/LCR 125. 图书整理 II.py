class CQueue(object):
    """
    https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/description/
    队列
    用栈实现队列
    """

    def __init__(self):
        self.soreted_list = []
        self.reverse_list = []

    def appendTail(self, value):  # push
        """
        :type value: int
        :rtype: None
        """

        for _ in range(len(self.reverse_list)):
            self.soreted_list.append(self.reverse_list.pop())

        self.soreted_list.append(value)
        for _ in range(len(self.soreted_list)):
            self.reverse_list.append(self.soreted_list.pop())

    def deleteHead(self):  # pop
        """
        :rtype: int
        """
        try:
            return self.reverse_list.pop()
        except:
            return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
