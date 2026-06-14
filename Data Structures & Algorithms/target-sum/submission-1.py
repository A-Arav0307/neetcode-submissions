class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = []

        def dfs(i, path, val):
            if i == len(nums) and val == target:
                res.append(nums.copy())
                return

            if i == len(nums):
                return
            
            path.append(nums[i])

            dfs(i+1, path, val + nums[i])   
            path.pop()
            path.append(-nums[i])
            dfs(i+1, path, val - nums[i])

        dfs(0, [], 0)
        return len(res)

