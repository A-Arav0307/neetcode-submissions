class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        value_list = [0] * n
        value_list[0] = nums[0]

        for i in range(0, n-1):
            if nums[i+1] > value_list[i]:
                value_list[i+1] = max(nums[i+1], nums[i+1] + value_list[i])
            else:
                value_list[i+1] = value_list[i] + nums[i+1]

        return value_list[n-1]