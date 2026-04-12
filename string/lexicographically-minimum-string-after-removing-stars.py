class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(26):
            stack.append([])

        removed = [False] * len(s)

        for i, ch in enumerate(s):
            if ch != '*':
                stack[ord(ch) - ord('a')].append(i)
            else:
                removed[i] = True
                for c in range(26):
                    if stack[c]:
                        idx = stack[c].pop()
                        removed[idx] = True
                        break

        result = []
        for i, ch in enumerate(s):
            if not removed[i]:
                result.append(ch)

        return "".join(result)