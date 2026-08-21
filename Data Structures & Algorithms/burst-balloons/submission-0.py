class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums = [1] + nums + [1] 

        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            
            if l > r:
                return 0 

            dp[(l, r)] = 0
            for i in range(l+1, r): 
                coins = nums[i] * nums[l] * nums[r] 
                coins += dfs(l, i) + dfs(i, r) 
            
                dp[(l, r)] = max(dp[(l,r)], coins)

            return dp[(l, r)] 

        return dfs(0, len(nums)-1) 