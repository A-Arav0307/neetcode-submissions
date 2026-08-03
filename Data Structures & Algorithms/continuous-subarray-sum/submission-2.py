class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        diff = {}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            remainder = prefix % k
            if remainder in diff:
                if i - diff[remainder] >= 2:
                    return True
            else:
                diff[remainder] = i
             
            

        return False
