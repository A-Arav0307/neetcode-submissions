class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final_list = []

        def dfs(values, i):
            if len(values) == len(nums):
                final_list.append(values.copy())
                return 
            if i == len(nums):
                return 

            for num in nums:
                if num in values:
                    continue
                values.append(num)
                dfs(values)
                values.pop()
              

        dfs([])
        return final_list

            
            