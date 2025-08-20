class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for c in range(26):
            char = chr(c + ord('a'))
            start = s.find(char)
            if start == -1:
                continue
            end = s.rfind(char)
            if end - start <= 1:
                continue
            cnt += len(set(s[start+1: end]))
        return cnt