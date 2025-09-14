class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 0
        for i in range(len(s)):
            if s[i] in 'aeiou':
                vowels += 1
        return vowels != 0
