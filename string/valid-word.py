class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")
        v = c = 0

        for ch in word:
            if ch.isdigit():
                continue
            elif ch.isalpha():
                if ch in vowels:
                    v += 1
                else:
                    c += 1
            else:
                return False
        return v > 0 and c > 0