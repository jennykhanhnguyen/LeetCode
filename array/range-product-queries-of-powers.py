class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        CONST = 10**9+7
        power = []
        ans = []
        for i in range (30):
            if (n >> i) & 1:
                power.append(2**i)
        for left, right in queries:
            val = 1
            for i in range (left, right +1):
                val *= power[i]
            val = val%CONST
            ans.append(val)
        return ans


        