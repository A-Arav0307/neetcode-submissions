class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        value = 0 
        l, r = 0, 0 
        for r in range(len(nums)):
            value += nums[r]
            while value >= target:
                value -= nums[l]
                length = min(length, r-l+1)
                l += 1
        
        return length if length != float('inf') else 0
        