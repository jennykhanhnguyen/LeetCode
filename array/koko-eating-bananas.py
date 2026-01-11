class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def can_finish_eating(piles, h, k):
            hours_used = 0
            for p in piles:
                hours_used += ceil(float(p)/k)
            return hours_used <= h

        left, right = 1, 1000000000 # 10^9 max pile size
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if can_finish_eating(piles, h, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans