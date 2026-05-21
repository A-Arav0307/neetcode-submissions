class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final_dict = {}
        for num in nums:
            if num not in final_dict.keys():
                final_dict[num] = 1
            else:
                final_dict[num] += 1
        
        for value in final_dict.values():
            if value > 1:
                return True
        return False

    