from collections import defaultdict 
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = defaultdict(int) 
        ways = 0 
        freq[0] = 1
        curr = 0
        for num in nums: 
            curr += num
            need = curr - goal 
            ways += freq.get(need, 0) 
            freq[curr] += 1
        
        return ways