class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        for i in range(1,len(s)):
            count0 = 0
            count1 = 0
            left = s[:i]
            right = s[i:]
            result.append(left.count('0') + right.count('1'))
        result.sort()
        return result[-1]
                    

       
        