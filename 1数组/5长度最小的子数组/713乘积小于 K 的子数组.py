from typing import List


class Solution:
    """
    https://leetcode.cn/problems/subarray-product-less-than-k/description/
    https://leetcode.cn/problems/subarray-product-less-than-k/solutions/1163012/713-cheng-ji-xiao-yu-kde-zi-shu-zu-by-bl-k5rc/
    """
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        prod = 1
        ans = 0

        if k < 1:
            return 0

        for r, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod //= nums[l]
                l += 1
            ans += (r - l + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    a = s.numSubarrayProductLessThanK(nums, k)
    print(a)
