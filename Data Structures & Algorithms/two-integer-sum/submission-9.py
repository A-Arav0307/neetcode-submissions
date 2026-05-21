# for enumerate, index goes first then value. index, value.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, value in enumerate(nums):
            if (target - value) in my_dict: 
                return [my_dict[target-value], index]
            my_dict[value] = index 
        return []
