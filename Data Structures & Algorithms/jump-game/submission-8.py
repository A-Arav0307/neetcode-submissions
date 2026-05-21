class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        j = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0 or i + nums[i] < j:
                continue
            else:
                j = i
        if j == 0:
            return True 
        return False
            