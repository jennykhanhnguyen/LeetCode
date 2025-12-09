class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = set()
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] in char:
                while s[right] in char:
                    char.remove(s[left])
                    left += 1
                char.add(s[right])

            elif s[right] not in char:
                char.add(s[right])
            res = max(res, right-left +1)
        return res