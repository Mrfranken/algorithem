class Solution(object):
    """
    最极限的情况是 arr是完整连续的数组，缺失值应该就是arr的最大值 加 k
    """
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        range_list = list(range(1, arr[-1] + k + 1))
        for num in arr:
            range_list[num - 1] = 0

        count = 0
        for item in range_list:
            if item != 0:
                count += 1

            if count == k:
                return item


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    k = 2
    print(Solution().findKthPositive(arr, k))
