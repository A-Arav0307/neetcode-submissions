class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = max(nums[0], nums[1])
        for i in range(1, len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            if currSum < 0: 
                currSum = 0 
            

        return maxSum