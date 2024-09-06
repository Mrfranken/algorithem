class Solution(object):

    def fs(self, query):
        d = {}
        for item in query:
            d[item] = d.get(item, 0) + 1
        sorted_d = sorted(d.items(), key=lambda x: x[0])
        return sorted_d[0][-1]

    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        words_du = [self.fs(word) for word in words]
        res = []
        for query in queries:
            du = 0
            query_du = self.fs(query)
            for word_du in words_du:
                if query_du < word_du:
                    du += 1
            res.append(du)
        return res


if __name__ == '__main__':
    s = Solution()
    queries = ["bbb", "cc"]
    words = ["a", "aa", "aaa", "aaaa"]
    print(s.numSmallerByFrequency(queries, words))
