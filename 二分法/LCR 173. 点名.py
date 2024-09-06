class Solution(object):
    def takeAttendance(self, records):
        """
        :type records: List[int]
        :rtype: int
        https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/solutions/155915/mian-shi-ti-53-ii-0n-1zhong-que-shi-de-shu-zi-er-f/
        二分法
        """
        left, right = 0, len(records) - 1
        while left <= right:
            mid = (left + right) // 2
            if records[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    s = Solution()
    records = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]
    print(s.takeAttendance(records))
