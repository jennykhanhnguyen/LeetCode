import re
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        pattern1 = r"(\d+)\[([a-z]+)\]"
        pattern2 = r"(\d+)\[(.+?)\]"

        if '[' not in s:
            return s

        # 3[abc]
        match1 = re.search(pattern1, s)
        if match1:
            num = int(match1.group(1)) # 3
            text = match1.group(2) # "abc
            decoded = num * text # "abcabcabc"
            
            new_s = s[:match1.start()] + decoded + s[match1.end():]
            return self.decodeString(new_s)

        # # 3[a2[c]]
        # match2 = re.search(pattern2, s)
        # if match2:
        #     num = int(match2.group(1)) # 3
        #     inside = match2.group(2) #a2[c
        #     print(inside)
        #     inside_decoded = self.decodeString(inside) # acc
        #     decoded = num * inside_decoded # accaccacc

        #     new_s = s[:match2.start()] + decoded + s[match2.end():]
        #     return self.decodeString(new_s)
        return s
