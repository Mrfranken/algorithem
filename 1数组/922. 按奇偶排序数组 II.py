class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_index = 0
        odd_index = 1
        res = [None] * len(nums)
        for num in nums:
            if num % 2:
                # 偶数
                res[odd_index] = num
                odd_index += 2
            else:
                # 奇数
                res[even_index] = num
                even_index += 2
        return res


if __name__ == '__main__':
    nums = [4, 2, 5, 7]
    s = Solution()
    print(s.sortArrayByParityII(nums))
