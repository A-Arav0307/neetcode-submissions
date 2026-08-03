class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        j = 0
        while j < len(nums)-1:
            if nums[j] == 0:
                return False
            j += nums[j]

        return True 

        
