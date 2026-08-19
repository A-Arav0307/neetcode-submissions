class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, value):
            if i == len(coins) or value > amount:
                return 0

            if value == amount:
                return 1

            if (i, value) in memo:
                return memo[(i, value)]

            memo[(i, value)] = dfs(i, value + coins[i]) + dfs(i+1, value) 

            return memo[(i, value)]



        return dfs(0, 0)
