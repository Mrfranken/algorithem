class MyQueue(object):

    def __init__(self):
        self.sort_list = []
        self.reverse_list = []

    def push(self, x):

        for item in self.reverse_list:
            self.sort_list.append(self.reverse_list.pop())

        self.sort_list.append(x)

        for item in self.sort_list:
            self.reverse_list.append(self.sort_list.pop)

    def pop(self):
        self.reverse_list.pop()

    def peek(self):
        return self.reverse_list[-1]

    def empty(self):
        return len(self.reverse_list) == 0
