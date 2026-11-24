class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) 
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        value_list = [0] * n
        value_list[0] = nums[0]
        value_list[1] = max(nums[0], nums[1])

        for i in range(2, n):
            value_list[i] = max(value_list[i-1], nums[i] + value_list[i-2])

        return value_list[n-1]
