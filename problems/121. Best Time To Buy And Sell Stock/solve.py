class Solution:
    def maxProfit(self,prices):
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(profit, max_profit)
            else:
                buy = sell
            sell += 1
        return max_profit
