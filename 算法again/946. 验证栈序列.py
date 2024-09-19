class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        for index, value in enumerate(pushed):
            while stack and stack[-1] == popped[0]:
                stack.pop()
                del popped[0]
            stack.append(value)
            if value == popped[0]:
                del popped[0]
                stack.pop()

        while stack:
            if stack[-1] == popped[0]:
                del popped[0]
                stack.pop()
            else:
                return False
        return False if stack else True


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    pushed = [2, 3, 0, 1]
    popped = [4, 5, 3, 2, 1]
    popped = [4, 3, 5, 1, 2]
    popped = [0, 3, 2, 1]
    print(Solution().validateStackSequences(pushed, popped))
