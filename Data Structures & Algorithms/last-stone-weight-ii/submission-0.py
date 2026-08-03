class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= len(stones) or j >= len(stones):
                memo[(i,j)] = False
            if i == j: 
                memo[(i,j)] = False

            if stones[i] - stones[j] < 0:
                stones[j] -= stones[i]
                stones.pop(i)

            elif stones[i] - stones[j] > 0:
                stones[i] -= stones[j]
                stones.pop(j)

            elif stones[i] == stones[j]:
                if i < j:
                    stones.pop(i)
                    stones.pop(j-1)
                elif j < i:
                    stones.pop(j)
                    stones.pop(i-1)

            memo[(i, j)] = True 

            dfs(i+1, j) 
            dfs(i, j+1) 

        dfs(0,0)
        return stones[-1] if stones else 0 

