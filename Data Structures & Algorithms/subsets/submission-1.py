class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        def backtrack(i, curr):
            if i == len(nums): 
                final_list.append(curr.copy())
                return 
                
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
            backtrack(i+1, curr) 

        backtrack(0, [])
        return final_list