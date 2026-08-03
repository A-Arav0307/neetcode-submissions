from collections import defaultdict 
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        diff = defaultdict(int)
        diff[0] = 1
        subarrays = 0
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]
            need = curr % k 
            subarrays += diff.get(need, 0)
            diff[need] += 1

        return subarrays