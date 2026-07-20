from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        frequency = defaultdict(int)
        frequency[0] = 1

        current_sum = 0
        subarrays = 0

        for num in nums:
            current_sum += num 
            if current_sum - k in frequency:
                subarrays += frequency[current_sum - k]
            frequency[current_sum] += 1

        return subarrays

