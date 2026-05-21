class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        maxVal = nums[0]
        value = nums[0]

        for i in range(1, n):
            value = max(nums[i], nums[i] + value)
            maxVal = max(maxVal, value)

        return maxVal