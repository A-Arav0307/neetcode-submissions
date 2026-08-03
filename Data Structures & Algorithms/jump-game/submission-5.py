class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        j = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue
            if i + nums[i] < j:
                return False
            if i + nums[i] >= j:
                j = i
        if j == 0:
            return True 
        return False
            