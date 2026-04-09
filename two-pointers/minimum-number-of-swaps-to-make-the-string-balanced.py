import math
class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = 0
        stack = []
        for i in range(len(s)):
            if s[i] == "[":
                stack.append(s[i])
            else:
                if len(stack) == 0: 
                    cnt += 1
                else:
                    stack.pop()
        return math.ceil((len(stack) + cnt)/4)
