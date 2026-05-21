class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, value in enumerate(nums): 
            #when adding things to a dictionary, check if what you want 
            #is already in the dictionary before adding an entry
            difference = target - value
            if difference in my_dict: 
                return [my_dict[target - value], index]
            
            my_dict[value] = index 
        

        
