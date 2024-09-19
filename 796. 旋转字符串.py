class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        first_letter = goal[0]
        for index, letter in enumerate(s):
            if letter == first_letter:
                if s[index:] + s[:index] == goal:
                    return True
        return False


if __name__ == '__main__':
    s = "abcde"
    goal = "cdeab"
    print(Solution().rotateString(s, goal))
