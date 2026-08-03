class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_list = []


        def dfs(curr, i): 
            if i >= len(nums):
                final_list.append(curr.copy())
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                
                curr.append(nums[j])
                dfs(curr, i+1)
                curr.pop()
  

        dfs([], 0)
        return final_list
