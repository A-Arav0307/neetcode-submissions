class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
            
        target = sum(nums) // 2
        memo = {}
        
        def dfs(i, val):
            if (i, val) in memo:
                return memo[(i, val)]
            if val == target:
                return True
            if val > target or i >= len(nums):
                return False
                
            # Compute both choices for the current state
            take = dfs(i + 1, val + nums[i])
            skip = dfs(i + 1, val)
            
            # Save the result for the CURRENT state (i, val)
            memo[(i, val)] = take or skip
            return memo[(i, val)]
            
        return dfs(0, 0)
