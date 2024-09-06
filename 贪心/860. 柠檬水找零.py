class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        https://leetcode.cn/problems/lemonade-change/solutions/855205/860ning-meng-shui-zhao-ling-pythontan-xi-bj83/
        8.13 贪心
        """
        cash = {}
        for index, bill in enumerate(bills):
            if not cash and bill != 5:
                return False
            elif bill == 5:
                if bill not in cash:
                    cash[bill] = 1
                else:
                    cash[bill] += 1
                continue
            else:
                zhaolin = bill - 5
                while zhaolin:
                    if zhaolin == 15 and cash.get(10, 0):
                        cash[10] -= 1
                        zhaolin -= 10
                    elif zhaolin >= 5 and cash.get(5, 0):
                        cash[5] -= 1
                        zhaolin -= 5
                    else:
                        return False
            if bill not in cash:
                cash[bill] = 1
            else:
                cash[bill] += 1
        return True


if __name__ == '__main__':
    s = Solution()
    bills = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]
    print(s.lemonadeChange(bills))
