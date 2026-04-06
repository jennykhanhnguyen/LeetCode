from collections import defaultdict 
class Solution:
    def mirror(self, character: str) -> str:
        return chr(ord('a') + ord('z') - ord(character)) 
    def calculateScore(self, s: str) -> int:
        dct = defaultdict(list)
        ans = 0
        for i in range(len(s)):
            if self.mirror(s[i]) in dct and len(dct[self.mirror(s[i])]) != 0:
                index = dct[self.mirror(s[i])].pop()
                ans += (i - index)
                # print(self.mirror(s[i]), index, i)
            else:
                dct[s[i]].append(i)
                # print(s[i], dct[s[i]],i)
        return ans 
        


