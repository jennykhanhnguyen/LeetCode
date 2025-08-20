class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # 1 <= i <= limit + 1
        # j - i - 1 <= limit #
        # j - i - 1 = limit
        # j = i + limit + 1
        # m + n - limit - 1 <=  j <= m + n - 1
        # ^^^^ lower_bound
        # max(j - lower_bound - 1, 0) 
        # 1 2 3 4 5 6 7
        m = n
        n = 3
        lower_bound = max(m + n - limit - 1, 1)
        ans = 0
        for i in range(1, min(limit + 2, m + n)):
            j = min(i + limit + 1, m + n - 1)
            ans += min(max(j - lower_bound + 1, 0), j - i)
        return ans