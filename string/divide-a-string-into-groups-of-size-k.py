class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        lst = []
        i = 0
        cnt = 0
        while i+k <= len(s):
            st = ''
            for m in range (k):
                st += s[i+m]
                cnt += 1
            lst.append(st)
            i += k 
        if cnt < len(s):
            st = ''
            for n in range (cnt,len(s)):
                st += s[n]
            for m in range (len(s)-cnt, k*(len(s)//k+1)-cnt):
                st += fill
            lst.append(st)
        return lst

