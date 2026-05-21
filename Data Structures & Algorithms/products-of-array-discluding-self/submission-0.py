class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = [1] * len(nums)
        prefix_value = 1
        for num in range(len(nums)-1):
            prefix_list[num+1] = prefix_value * nums[num]
            prefix_value *= nums[num]
        
        #running postfix 
        multiplier = 1
        for index in range(len(nums)-1, 0, -1):
            multiplier *= nums[index]
            prefix_list[index-1] = multiplier * prefix_list[index-1]

        
        return prefix_list


        

