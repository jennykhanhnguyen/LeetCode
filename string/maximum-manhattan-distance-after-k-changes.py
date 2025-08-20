
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
         
        def find_maxDist(d, k):
            # L, R 
            if d['N'] >= d['S']:
                tmp = min(d['S'], k)
                d['N'] += tmp
                d['S'] -= tmp
                k -= tmp
            else:
                tmp = min(d['N'], k)
                d['S'] += tmp
                d['N'] -= tmp
                k -= tmp
            
            if d['E'] >= d['W']:
                tmp = min(d['W'], k)
                d['E'] += tmp
                d['W'] -= tmp
                k -= tmp
            else:
                tmp = min(d['E'], k)
                d['W'] += tmp
                d['E'] -= tmp
                k -= tmp
            
            return abs(d['N'] - d['S']) + abs(d['E'] - d['W'])
            
        
        
        # d = [0, 0, 0, 0]
        d = {"N":0, "S":0, "E":0, "W":0}
        # "NWSE"
        ans = 0
        for i in range(len(s)):
            d[s[i]] += 1
            # print(d)
            ans = max(ans, find_maxDist(d.copy(), k))
        return ans 