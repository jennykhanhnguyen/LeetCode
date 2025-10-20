class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    # large number (more than max amount)
        inf = amount + 1
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != inf else -1
