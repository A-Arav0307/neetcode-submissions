class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(i):
            if i >= len(nums)-1:
                return True 
            if nums[i] == 0:
                memo[i] = False
                return False 
            if i in memo:
                return memo[i]

            for j in range(i+1, i+nums[i]+1):
                if dfs(j): 
                    memo[j] = True
                    return True
            memo[i] = False
            return False

        return dfs(0)