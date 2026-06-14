class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_list = []

        def backTrack(i, lst):
            if i == len(nums):
                final_list.append(lst.copy())
                return
            
            #choice 1 -- add number to left branch
            lst.append(nums[i])
            backTrack(i+1, lst)
            lst.pop()

            #choice 2 -- keep same list
            backTrack(i+1, lst)

        backTrack(0, [])
        return final_list