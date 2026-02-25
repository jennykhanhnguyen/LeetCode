import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/k)
            if h >= total:
                return True
            return False
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2            
            if can_finish(mid):
                answer = mid        
                right = mid - 1     
            else:
                left = mid + 1      
        
        return answer
