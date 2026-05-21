class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = len(prices) - 1 
        max_value = 0

        for i in range(len(prices)-1, -1, -1):
            if prices[i] - prices[j] < 0:
                continue
            while j >= 0 and (prices[i] - prices[j]) >= 0:
                max_value = max(max_value, prices[i]-prices[j])
                j -= 1

                

        return max_value