class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        self.profit = 0
        
        def dfs(index, buying):
            if (index, buying) in memo: 
                return memo[(index, buying)] 

            if index >= len(prices):
                return 0
            
            if buying:
                memo[(index, buying)] = max(dfs(index+1, False) - prices[index], dfs(index+1, True))

            elif not buying:
                memo[(index, buying)] = max(dfs(index+2, True) + prices[index], dfs(index+1, False))
                        
            return memo[(index, buying)]

        return dfs(0, True) 