class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = max(nums)
        currMax, currMin = 1, 1
        for i in range(len(nums)):
            if nums[i] == 0:
                currMax = 1
                currMin = 1
                continue
            temp = currMax * nums[i]
            currMax = max(nums[i] * currMax, nums[i] * currMin, nums[i])
            currMin = min(temp, nums[i] * currMin, nums[i])
        

            max_val = max(max_val, currMax)

        return max_val