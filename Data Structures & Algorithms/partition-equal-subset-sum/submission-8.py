class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False 

        memo = {}
        def dfs(i, val):
            if i >= len(nums) or val > (total / 2):
                memo[(i, val)] = False
                return False

            if val == total / 2:
                memo[(i, val)] = True 
                return True

            if i in memo:
                return memo[(i, val)]
            
            dfs(i+1, val+nums[i]) 
            dfs(i+1, val) 
            memo[(i, val)] = True
            return True

        return dfs(0, 0) 
        