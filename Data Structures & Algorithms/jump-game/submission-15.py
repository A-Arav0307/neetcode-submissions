class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        j = 0

        for i in range(len(nums)):
            furthest = j + nums[j]
            if furthest >= len(nums)-1:
                return True 
            j += nums[j]

        return False