class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, val):
            if i == len(nums):
                if val == target:
                    return 1
                return 0
            
            if (i, val) in memo:
                return memo[(i, val)]
        
            left = dfs(i+1, val + nums[i])   
            right = dfs(i+1, val - nums[i])

            memo[(i, val)] = left + right
            return memo[(i, val)]

        return dfs(0, 0)
        

