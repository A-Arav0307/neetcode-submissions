class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[-1])

        for l in range(len(nums)): 
            for r in range(l, len(nums)):
                if prefix[r+1] - prefix[l] == k:
                    subarrays += 1


        return subarrays