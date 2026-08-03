class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for val in nums: 
            my_dict[val] = target-val

        for key, item in my_dict.items(): 
            if key in nums and (target-val) in nums: 
                my_list = [nums.index(key), nums.index(target-val)]
                my_list.sort()
                return my_list

        return 0
