class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if currSum < 0: 
                currSum = 0 
            currSum += nums[i]
            maxSum = max(maxSum, currSum, nums[i])
            
            

        return maxSum