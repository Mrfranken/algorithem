# -*- utf-8 -*-

prices = [3, 15, 6, 14]


# 算法入口
def getResult():
    # 记录题解
    list_length = len(prices)
    # res = [-1] * list_length
    res = []
    res.extend(prices)

    # 单调栈，栈底到栈顶单调递增，压栈元素是栈顶元素在nums顺序后面的值
    # 每当压栈时，比较栈顶元素 > 压栈元素？若是，则说明找到了栈顶元素的下一个更小值，此时弹栈，压栈元素继续和新栈顶元素比较大小，直到栈顶元素 <= 压栈元素，则停止比较，执行压栈
    stack = []
    # 这里循环两轮，因为一轮循环可能无法确保所有值都能找到下一个更小值
    for current_index in range(list_length * 2):
        # prices_j 是压栈(索引对应的)元素
        current_price = prices[current_index % list_length]  # 索引 current_index % n 是为了让第二轮遍历时，继续从prices的0索引开始

        while len(stack) > 0:
            # prices[i] 是栈顶(索引对应的)元素
            top = stack[-1]

            if prices[top] > current_price:
                # 如果栈顶元素 > 压栈元素，则说明找到了栈顶元素的下一个更小值，此时栈顶元素弹出,压栈元素继续和新的栈顶元素比较
                stack.pop()
                # 题目要统计当前元素和其下一个更小值元素之和
                res[top] = prices[top] + current_price
            else:
                break

        # 只有第一轮遍历时，才允许压栈，第二轮遍历时，只进行比较
        if current_index < list_length:
            stack.append(current_index)

    return " ".join(map(str, res))


# 算法调用
print(getResult())

# class Solution(object):
#     def nextGreaterElements(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         N = len(nums)
#         res = [-1] * N
#         stack = []
#         for i in range(N * 2):
#             while stack and nums[stack[-1]] < nums[i % N]:
#                 res[stack.pop()] = nums[i % N]
#             stack.append(i % N)
#         return res
#
#
# s = Solution()
# s.nextGreaterElements([1, 2, 3, 4, 3])
