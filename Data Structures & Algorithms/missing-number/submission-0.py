class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        for num in range(n):
            if num ^ nums[num] != 0:
                return num