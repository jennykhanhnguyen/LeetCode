class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i, price in enumerate(prices):
            if price < buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy
        return profit
