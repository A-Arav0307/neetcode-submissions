class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-coin])

        
        if dp[amount] > amount + 1:
            return -1
        return dp[amount]