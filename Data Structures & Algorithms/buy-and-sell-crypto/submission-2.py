class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            best = min(best, prices[i]) 
            profit = max(profit, prices[i] - best)

        return profit 