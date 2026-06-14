class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        visited = set()

        def dfs(curr):
            if len(curr) == len(nums):
                final_list.append(curr.copy())
                return 

            for num in nums:
                if num in visited:
                    continue 

                curr.append(num)
                visited.add(num)
                dfs(curr)
                curr.pop()
                visited.remove(num)

        dfs([])
        return final_list