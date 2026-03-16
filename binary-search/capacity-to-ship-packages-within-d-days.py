class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(max_val):
            current = 0 
            day = 1
            for i in range(len(weights)):
                if current + weights[i] > max_val:
                    current = weights[i]
                    day += 1
                else:
                    current += weights[i]
            return day
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if check(mid) <= days:
                right = mid
            else:
                left = mid + 1
        return left 

