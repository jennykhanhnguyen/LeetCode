class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        dic = Counter(words)
        pal = 0
        double = False
        for key, val in dic.items():
            if key[0] == key[1]:
                pal += val//2*4
                if val % 2 == 1:
                    double = True
            elif key[0]<key[1]:
                rev = key[1] + key[0]
                pal += min(val, dic[rev]) * 4
        return pal + double * 2 



