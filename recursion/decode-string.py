class Solution:
    def decodeString(self, s: str) -> str:
        prefix, k = "", 0
        stack = []

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == "[":
                stack.append((prefix, k))
                k = 0
                prefix = ""
            elif ch.isalpha():
                prefix += ch
            elif ch == "]":
                prev_prefix, prev_k = stack.pop()
                prefix = prev_prefix + prev_k * prefix
            print(k,stack,prefix)

        return prefix