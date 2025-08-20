class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for char in s:
            if char not in pairs: # open
                brackets.append(char)
            elif not brackets or brackets[-1] != pairs[char]: # close and not found matching brackets
                return False
            else: # close and found matching brackets
                brackets.pop()

        return len(brackets) == 0
