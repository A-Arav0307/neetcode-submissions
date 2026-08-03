class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1
        
        list_lengths = []
        for num in frequency:
            length = 0
            while num+1 in frequency:
                length += 1
                num = num + 1
            list_lengths.append(length)

        return max(list_lengths) + 1
