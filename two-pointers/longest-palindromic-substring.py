class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        dp = [False] * n
        start = 0
        max_len = 1

        for j in range(n):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1]):
                    dp[i] = True
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start = i
                else:
                    dp[i] = False

        return s[start:start + max_len]
