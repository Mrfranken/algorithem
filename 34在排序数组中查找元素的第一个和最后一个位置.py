from typing import List


# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         d = {}
#         for index, value in enumerate(nums):
#             v = d.get(value, None)
#             if v is None:
#                 d[value] = [index]
#             else:
#                 d[value].append(index)
#         v = d.get(target, None)
#         if not v:
#             return [-1, -1]
#         if len(v) == 1:
#             return v * 2
#         return [v[0], v[-1]]


# lower_bound 返回最小的满足 nums[i] >= target 的 i
# 如果数组为空，或者所有数都 < target，则返回 len(nums)
# 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

# # 闭区间写法
# def lower_bound(nums: List[int], target: int) -> int:
#     left, right = 0, len(nums) - 1  # 闭区间 [left, right]
#     while left <= right:  # 区间不为空
#         # 循环不变量：
#         # nums[left-1] < target
#         # nums[right+1] >= target
#         mid = (left + right) // 2
#         if nums[mid] < target:
#             left = mid + 1  # 范围缩小到 [mid+1, right]
#         else:
#             right = mid - 1  # 范围缩小到 [left, mid-1]
#     return left  # 或者 right+1


# # 左闭右开区间写法
# def lower_bound2(nums: List[int], target: int) -> int:
#     left = 0
#     right = len(nums)  # 左闭右开区间 [left, right)
#     while left < right:  # 区间不为空
#         # 循环不变量：
#         # nums[left-1] < target
#         # nums[right] >= target
#         mid = (left + right) // 2
#         if nums[mid] < target:
#             left = mid + 1  # 范围缩小到 [mid+1, right)
#         else:
#             right = mid  # 范围缩小到 [left, mid)
#     return left  # 或者 right


# # 开区间写法
# def lower_bound3(nums: List[int], target: int) -> int:
#     left, right = -1, len(nums)  # 开区间 (left, right)
#     while left + 1 < right:  # 区间不为空
#         mid = (left + right) // 2
#         # 循环不变量：
#         # nums[left] < target
#         # nums[right] >= target
#         if nums[mid] < target:
#             left = mid  # 范围缩小到 (mid, right)
#         else:
#             right = mid  # 范围缩小到 (left, mid)
#     return right  # 或者 left+1


# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         start = lower_bound(nums, target)  # 选择其中一种写法即可
#         if start == len(nums) or nums[start] != target:
#             return [-1, -1]
#         # 如果 start 存在，那么 end 必定存在
#         end = lower_bound(nums, target + 1) - 1
#         return [start, end]


class Solution(object):
    def searchRange1(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            num = nums[middle]
            if target <= num:  # 注意这里 34 题的条件跟 704 35题不同
                right = middle - 1
            else:
                left = middle + 1
        return left

    def searchRange(self, nums, target):
        start = self.searchRange1(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.searchRange1(nums, target + 1)
        return [start, end - 1]


if __name__ == '__main__':
    s = Solution()
    l = nums = [5, 7, 7, 8, 8, 10]
    # l = [3, 3, 3]
    l = [1, 1, 2]
    v = s.searchRange(l, 1)
    print(v)
