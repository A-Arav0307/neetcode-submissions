class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0 and i != len(nums) - 1:
                return False
            
            i += nums[i]
        

        return True