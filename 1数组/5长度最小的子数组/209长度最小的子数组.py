from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # left = 0
        # res = len(nums) + 1
        #
        # tmp = 0
        # for right, num in enumerate(nums):  # num = nums[index]
        #     tmp += num
        #
        #     while tmp >= target:
        #         res = min(res, right - left + 1)
        #         tmp -= nums[left]
        #         left += 1
        #
        # return res if res < len(nums) else 0

        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0  # 当前的累加值

        while right < l:
            cur_sum += nums[right]

            while cur_sum >= target:  # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != float('inf') else 0


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    s = Solution()
    a = s.minSubArrayLen(target, nums)
    print(a)



