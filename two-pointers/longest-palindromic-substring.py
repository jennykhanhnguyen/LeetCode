class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = s[0]  

        for l in range(n):
            for r in range(n-1, l, -1):
                if r - l + 1 <= len(res):
                    break
                sub = s[l:r+1]
                if sub == sub[::-1]:   
                    res = sub
                    break  
        return res
