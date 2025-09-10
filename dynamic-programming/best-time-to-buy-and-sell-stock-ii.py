class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                if i+2 < len(prices):
                    total += max(prices[i+1]-prices[i], prices[i+2]-prices[i+1])
                else:
                    total += prices[i+1]-prices[i]
        return total