from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        
        odd = 0
        res = 0
        
        for n in nums:
            if n % 2 == 1:
                odd += 1
            
            res += count[odd - k]
            count[odd] += 1
        
        return res