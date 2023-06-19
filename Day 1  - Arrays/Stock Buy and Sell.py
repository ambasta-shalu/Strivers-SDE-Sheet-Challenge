# Coded by Shalu Ambasta :)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = prices[0]
        maxprofit = 0

        for i in range(len(prices)):
            profit = prices[i] - mini
            maxprofit = max(maxprofit, profit)
            mini = min(mini, prices[i])

        return maxprofit
        