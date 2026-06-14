class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        #add every single number to the dictionary initially
        for num in nums: 
            if num in my_set:
                return True
            my_set.add(num)

        return False

"""
Previous code: 
for num in nums: 
    if num not in my_dict: 
        my_dict[num] = 1

    if num in my_dict.keys(): 
        return True

The wrong part about this code is that you add num to the dictionary and 
immediately check if it is in my_dict, which means true is always returned. 

first add num to dict and then check if it is in the code. 

"""
