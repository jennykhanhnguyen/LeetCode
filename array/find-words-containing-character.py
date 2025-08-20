class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        arr = []
        for ind, word in enumerate(words):
            if x in word:
                arr.append(ind)
        return arr
