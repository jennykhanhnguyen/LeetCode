class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            rem = num % k
            for prev in range(k):
                dp[prev][rem] = dp[rem][prev] + 1
                res = max(res, dp[prev][rem])
        return res