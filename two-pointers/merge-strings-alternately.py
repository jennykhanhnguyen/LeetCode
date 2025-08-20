class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newstr = ''
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                newstr += word1[i]
                i += 1
            if j < len(word2):
                newstr += word2[j]
                j += 1
        return newstr
        