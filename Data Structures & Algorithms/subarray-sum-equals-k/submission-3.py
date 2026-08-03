class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        frequency = {0:1}
        current = 0
        for i in range(len(nums)):
            current += nums[i]
            if nums[i] - k in frequency:
                subarrays += frequency[nums[i]-k]

            else:
                frequency[current] = 1

        return subarrays