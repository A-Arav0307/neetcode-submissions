class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        nums.sort()
        for num in range(n+1):
            if num ^ nums[num] != 0:
                return num