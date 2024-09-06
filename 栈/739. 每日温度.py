class Solution(object):
    """
    记住针对这种问题：
    1. 先区分是单调递减栈还是递增栈
    2. stack 栈中存放的是value的index，不是具体的某一个value
    """

    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []
        for index, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                res_index = stack.pop()
                res[res_index] = index - res_index
            stack.append(index)
        return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    s = Solution()
    print(s.dailyTemperatures(temperatures))
