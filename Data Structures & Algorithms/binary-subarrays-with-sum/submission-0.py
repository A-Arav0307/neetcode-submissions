from collections import defaultdict 
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = defaultdict(int) 
        ways = 0 
        freq[0] = 1
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            diff = goal - curr
            if diff in freq: 
                ways += freq[diff]
            freq[diff] += 1

        return ways 