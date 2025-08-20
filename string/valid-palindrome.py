class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word = ''
        
        for char in s:
            if char.isalnum():
                word += char.lower()

        re = word[::-1]

        return re == word