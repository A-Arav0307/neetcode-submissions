class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = []
        self.answer = 0

        def dfs(i, val):
            if i == len(nums) and val == target:
                self.answer += 1
                return

            if i == len(nums):
                return
        
            dfs(i+1, val + nums[i])   
            dfs(i+1, val - nums[i])

        dfs(0, 0)
        return self.answer

