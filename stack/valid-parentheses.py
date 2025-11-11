class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for char in s:
            if char in hm:
                stack.append(hm[char])
            elif len(stack) != 0 and char == stack[-1]:
                stack.pop()
            else: 
                return False
        return len(stack) == 0
    