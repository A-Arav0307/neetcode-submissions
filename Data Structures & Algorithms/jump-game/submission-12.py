class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        j = 0
        while j < len(nums)-1:
            old_num = nums[j]
            j += nums[j]
            if nums[j] == 0 and j < len(nums)-1:
                if old_num == 1: 
                    return False
                else:
                    j -= old_num
                    j += 1
        return True 

        
