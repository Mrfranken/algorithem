class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = ''
        tmp_num = ''
        for item in s:
            if item.isdigit():
                tmp_num = tmp_num + item
                continue

            if item == "]":
                tmp = ''
                while stack:
                    letter = stack.pop()
                    if letter != '[':
                        tmp = letter + tmp
                    else:
                        num = stack.pop()
                        tmp = tmp * int(num)
                        stack.append(tmp)
                        break
            else:
                if tmp_num:
                    stack.append(tmp_num)
                    tmp_num = ''
                stack.append(item)
        return ''.join(stack)


if __name__ == '__main__':
    s = "3[a2[c]]"
    s = "abc3[cd]xyz"
    s = "3[a]2[bc]"
    s = "100[leetcode]"
    solution = Solution()
    print(solution.decodeString(s))
