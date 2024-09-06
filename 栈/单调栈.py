class Solution:
    def monotonicStack(self, nums):
        n = len(nums)
        ans = [0] * n
        st = []

        for i, v in enumerate(nums):
            while st and v > nums[st[-1]]:
                prevI = st.pop()
                ans[prevI] = i
                # 还可以针对 prevI, i, nums[prevI], nums[i] 做些其他的处理
            st.append(i)

        return ans


if __name__ == '__main__':
    s = Solution()
    # 测试
    nums = [2, 1, 2, 4, 3]
    print(s.monotonicStack(nums))  # 输出: [4, 2, 4, 0, 0]
