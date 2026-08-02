class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        prefix = [0] * n 
        suffix = [0] * n 
        result = [0] * n 

        #building prefix and suffix arrays 
        curr = 1
        for i in range(len(nums)):
            curr *= nums[i]
            prefix[i] = curr
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            curr *= nums[i]
            suffix[i] = curr

        result[0] = suffix[1]
        result[-1] = prefix[-2]
        for i in range(1, len(nums)-1): 
            result[i] = suffix[i+1] * prefix[i-1]

        return result