class Solution(object):
    """
    记住针对这种问题：
    1. 先区分是单调递减栈还是递增栈
    2. stack 栈中存放的是value的index，不是具体的某一个value
    """

    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(temperatures))
