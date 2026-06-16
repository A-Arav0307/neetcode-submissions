class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum, max_sum = 0, float('-inf') 
        neg_max_sum = float('-inf')
        if len(nums) == 1:
            return nums[0]
        for num in nums: 
            curr_sum += num
            if curr_sum <= 0:
                neg_max_sum = max(neg_max_sum, curr_sum) 
                curr_sum = 0 
            max_sum = max(max_sum, curr_sum)
        return max_sum if max_sum > 0 else neg_max_sum 